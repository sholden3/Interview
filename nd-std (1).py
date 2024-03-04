import seeker as skr
from seeker import UserVectorDistribution
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from readdata import Network
import random
import argparse
import scipy.stats as st
from math import ceil


class Distr(UserVectorDistribution):
    def __init__(self, network):
        UserVectorDistribution.__init__(self)
        self.demand_matrix = network.demand_matrix  # each row is a scenario, each column a client/product demand pair
        self.m = len(self.demand_matrix)
        self.matrix = self.demand_matrix
        return

    def sample_n(self, num):
        if (num > self.m):
            print("Not enough samples in UserVectorDistribution")
            exit(999)
        ret = []
        for k in range(num):
            ret.append(self.matrix[k])
        return ret


class Design:
    def __init__(self, sites_file, intersite_file, products_file, customers_file, period_file
                 , demand_file, customer_lanes_file):
        self.network = Network(sites_file, intersite_file, products_file, customers_file, period_file
                               , demand_file, customer_lanes_file)

    def optimize(self, pID, uID):
        env = skr.Env("Seeker_Meinolf_Mac_213_lic.sio", pID, uID, stochastic=True)
        env.set_stochastic_parameters(self.network.number_scenarios, 0.99)
        number_dcs = self.network.number_existing_dcs + self.network.number_potential_dcs
        client_assignment = [env.categorical(0, number_dcs - 1) for _ in range(self.network.number_clients)]
        assignment_sc = [env.switch_condition(ca, number_dcs) for ca in client_assignment]
        assignment_bool = [[env.bool(ca, dc) for ca in assignment_sc] for dc in range(number_dcs)]
        dc_open = [env.sum(assignment_bool[cand + self.network.number_existing_dcs]) >= 1
                   for cand in range(self.network.number_potential_dcs)]
        opening_cost = env.sum([dc_open[cand] for cand in range(self.network.number_potential_dcs)])
        dis = Distr(self.network)
        scenarios = env.user_vector_distribution(dis)
        client_products = [[scenarios[p * self.network.number_clients + c] for c in range(self.network.number_clients)]
                           for p in range(self.network.number_products)]
        product_load = [[env.sum_if(client_products[p], assignment_sc, dc)
                         for p in range(self.network.number_products)] for dc in range(number_dcs)]
        throughput = [env.sum(product_load[dc]) for dc in range(number_dcs)]
        overdraft = [
            env.min([env.max_0(throughput[dc] - self.network.capacity[dc]), env.convert(0.05 * self.network.capacity[dc])])
            for dc in range(number_dcs)]
        severe_overdraft = [env.max_0(throughput[dc] - 1.05 * self.network.capacity[dc]) for dc in range(number_dcs)]
        penalty = [overdraft[dc] * self.network.l5penalty[dc] + severe_overdraft[dc] * self.network.g5penalty[dc]
                   for dc in range(number_dcs)]
        total_penalty = env.sum(penalty)
        dc_product_inbound_cost = [[env.min([product_load[dc][p] * self.network.ftl_cost[dc][p],
                                             env.max([product_load[dc][p], env.convert(self.network.rail_min[dc][p])])
                                             * self.network.rail_cost[dc][p]])
                                    for p in range(self.network.number_products)] for dc in range(number_dcs)]
        dc_inbound_cost = [env.sum(dc_product_inbound_cost[dc]) for dc in range(number_dcs)]
        inbound_cost = env.sum(dc_inbound_cost)
        client_load = [[assignment_bool[dc][c] * env.sum([client_products[p][c] * self.network.outbound_cost[dc][p][c]
                                                          for p in range(self.network.number_products)])
                        for c in range(self.network.number_clients)] for dc in range(number_dcs)]
        dc_outbound_cost = [env.sum(client_load[dc]) for dc in range(number_dcs)]
        outbound_cost = env.sum(dc_outbound_cost)
        transportation_cost = inbound_cost + outbound_cost
        total_cost = total_penalty + transportation_cost
        env.enforce_leq(opening_cost, 2)
        total_cost_std = env.aggregate_stdev(total_cost)
        exp_total_cost = env.aggregate_mean(total_cost)
        total_cost_risk = (exp_total_cost + total_cost_std)
        env.minimize(total_cost_risk/1e3, 60, 0)  # +std_total_cost, 300, 0)
        print("Exp total costs", exp_total_cost.get_value())
        print("Total costs risk", total_cost_risk.get_value())
        print("Opening", [self.network.dcs[self.network.number_existing_dcs + cand]
                          for cand in range(self.network.number_potential_dcs) if dc_open[cand].get_value() > 0])
        print("Assigning", end=" ")
        for ci in range(self.network.number_clients):
            c = self.network.clients[ci]
            print(c, "=", self.network.dcs[int(client_assignment[ci].get_value())], "  | ", end=" ")
        print()

        dat = total_cost.get_values()
        inb = inbound_cost.get_values()
        outb = outbound_cost.get_values()
        pen = total_penalty.get_values()
        print("dat", dat)
        print("Mean Costs", np.mean(dat), "| Mean Inbound", np.mean(inb), "Mean outbound", np.mean(outb))
        #datdf = pd.DataFrame([max(1e-9, k) for k in dat], columns=["Cost"])
        #x = sns.kdeplot(x=datdf["Cost"], cut=0)
        #plt.show()
        print("Penalties", pen)
        #datdf = pd.DataFrame([max(1e-9, k) for k in pen], columns=["Penalty"])
        #x = sns.kdeplot(x=datdf["Penalty"], cut=0)
        #plt.show()
        #datdf = pd.DataFrame([max(1e-9, k) for k in inb], columns=["Inbound"])
        #x2 = sns.kdeplot(x=datdf["Inbound"], cut=0)
        #plt.show()
        #datdf = pd.DataFrame([max(1e-9, k) for k in outb], columns=["Outbound"])
        #x3 = sns.kdeplot(x=datdf["Outbound"], cut=0)
        #plt.show()
        total_cost_90 = env.aggregate_quantile(total_cost,0.9,False)
        proxy_cost = (5*total_cost_90 + exp_total_cost)
        #total_cost_std = env.aggregate_stdev(total_cost)
        #total_cost_risk = (exp_total_costs + total_cost_std)
        total_cost_capped_90 = env.min([total_cost, total_cost_90])
        exp_total_cost_capped_90 = env.aggregate_mean(total_cost_capped_90)
        env.evaluate()
        print("One Sigma:", total_cost_risk.get_value())
        print("Cap90:", exp_total_cost_capped_90.get_value())
        print("90meanmix:", proxy_cost.get_value())
        print(env.get_number_evaluations())
        env.end()
        return

        #        std_total_cost = env.aggregate_stdev(total_cost)
        #        proxy = exp_total_cost + 2*std_total_cost

        # proxy = env.aggregate_quantile(total_cost, 0.75, False)
        env.minimize(total_cost, 60, 0)  # , 600, 0)
        env.end()
        return

        print("Exp total costs", exp_total_cost.get_value())  # , " Proxy costs", proxy.get_value())
        dat = total_cost.get_values()
        inb = inbound_cost.get_values()
        outb = outbound_cost.get_values()
        print(dat)
        print("Mean Costs", np.mean(dat), "| Mean Inbound", np.mean(inb), "Mean outbound", np.mean(outb))
        print("Opening Costs", opening_cost.get_value())
        print("Opening", [self.network.dcs[dc] for dc in range(number_dcs) if dc_open[dc].get_value() > 0])
        print("Assigning", end=" ")
        for ci in range(self.network.number_clients):
            c = self.network.clients[ci]
            print(c, "=", self.network.dcs[int(client_assignment[ci].get_value())], "  | ", end=" ")
        print()
        datdf = pd.DataFrame([max(1e-9, k) for k in dat], columns=["Cost"])
        x = sns.kdeplot(x=datdf["Cost"], cut=0)
        # datdf = pd.DataFrame([max(1e-9, k) for k in inb], columns=["Inbound"])
        # x2 = sns.kdeplot(x=datdf["Inbound"], cut=0)
        # datdf = pd.DataFrame([max(1e-9, k) for k in outb], columns=["Outbound"])
        # x3 = sns.kdeplot(x=datdf["Outbound"], cut=0)
        # ax.set_xlim((1500, 2600))
        plt.show()
        # env.minimize(opening_cost, 1, 0)
        # env.evaluate()
        # print(client_products[0][0].get_values())


#        print ([[client_products[p][c].get_values() for c in range(self.network.number_clients)]
#                for p in range(self.network.number_products)])
# env.end()


def main(sites_file, intersite_file, products_file, customers_file, period_file, demand_file, customer_lanes_file
         , pID, uID):
    design = Design(sites_file, intersite_file, products_file, customers_file, period_file
                    , demand_file, customer_lanes_file)
    design.optimize(pID, uID)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--pID', nargs='?', const=1, default="-1")
    parser.add_argument('--uID', nargs='?', const=1, default="0")
    args = parser.parse_args()
    main("gains/Sites-Table 1.csv", "gains/InterSiteLanes-Table 1.csv", "gains/Products-Table 1.csv"
         , "gains/Customers-Table 1.csv", "gains/Periods-Table 1.csv"
         , "gains/CustomerDemand-Table 1.csv", "gains/CustomerLanes-Table 1.csv", int(args.pID), int(args.uID))
