# In this section, we are diving into binary search trees. First thing we want to do is talk about why we want to use them.
# Arrays can manipulate the last item in O(1) constant running time complexity, which is exceptionally fast.
# Linked lists can manipulate the first item of the data structure fast.
# Searching for an arbitrary item takes O(N) linear running time for both data structures.
# What if the array data structure is sorted?
# We can search for arbitrary item in O(logN) logarithmic time complexity.
# This is the concept behind binary search.
# We can also break down arrays and linked lists as the following:
# Linked Lists
# Search O(N), Insert at the start O(1), Insert at the end O(N), waste space O(N).
# Arrays
# Search O(1), Insert at the start O(N), Insert at the end O(1), waste space 0.
# Irregardless of using arrays versus linked lists, remember that searching for an arbitrary item is going to be O(N) for both.
# So let us look at Trees (Graph Theory). A tree is a G(V,E) undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic
# undirected graph.
# We have access to the root node within it exclusively, and all other nodes can be accessed via the root node. Any node without a child is called the leaf node.
# We then have our edges connecting our vertices.
# This is very similar to what we have seen with linked lists. If we want to access other nodes of the link list, we have to start with the head node.
# Now if we have two paths to a single vertices, then this is not a tree. If there is a cycle, it is not a tree.
# We should also be able to define parent, children, relationships through this.

# Now what about Binary Search Trees
# Binary search trees have directed edges, to the parent nodes are pointing in the direction of the children.
# Every node within the tree itself can have, at most, 2 children (left child and right child).
# The left child is smaller than the parent node.
# The right child is greater than the parent node.
# We can access the root node exclusively, and all other nodes can be accessed via the root node.
# Every decision can get rid of half of the data (like with binary search) and this is how we can achieve O(logN) running time.
# So we have these features because we want to enforce this sorted order on our binary search data tree. Every decision allows us to get rid of half of the data,
# like with binary search. But this means that we must always enforce this order.
# This leads us to the Haith parameter. The Haith parameter of a tree is the number of edges on the longest downward path between the root node, and the given leaf node.
# So essentially the haith parameter, or the height of a tree, is the number of edges on the lognest downward path between the root and a leaf node. The number of layers the tree
# contains. We can view the layer as 2^(h-1) nodes. With the first being 2^0, second being 2^1, and so on.
# So to figure out how many N nods are there in a complete binary search tree with h height, we need to solve the following equation:
# 2^(h-1)=N
# log_2 2^(h-1)=log_2N
# h = log_2 N + 1
# h = O(logN) where this is the base 2 log of N, where we drop + 1.
# We need to keep the height of a tree at a minimum. The logarithmic O(logN) running time is valid only when the tree strcuture is balanced.
# We should keep the height of a tree minimum which is h=logN.
# The tree structure may become imbalanced which means the number of nodes significantly differ in the subtrees.
# If the tree is imbalanced, so the h=logN relation is no longer valid, then the operations' running time is no longer O(logN) logarithmic.
# If we have an imbalanced tree, the running time of operations may even be reduced to O(N) linear running time complexity.
# But for our balanced tree, the running time of operations are O(logN) always. Now, this doesn't mean that both sides have the same number of nodes, but that each side has the
# same height.
# Bineary Search Trees are data structures so the aim is to be able to store items efficiently.
# It keeps the keys in sorted order so that lookup, and other operations, can use the principle of binary search with O(logN) running time.
# Each comparison allows the operations to skip over half of the tree, so that each operation takes time proportional to the logarithm of the number of items stored in the tree.
# This is much better than O(N) linear time that is required to find items by key in an unsorted array, but slower than the corresponding operations on hash tables with O(1).

# So let us insert items into a binary search tree, and how to search for an arbitrary element.
# Let us say that we want to insert the value 12 into our empty binary search tree. Because it is empty, it becomes the head node. If we add another node, 4, we have to start at the
# root node, and have to look at if the node is greater than or less than the node. If it is greater than, it is on the right, if less than on the left. So we add it to the left.
# Now if we want to add 8, we compare it to 12, and it is on the left. We then look at 4, and it is greater than 4, so we create a new node attached to the right side of 4. 
# Adding 20 we add a node to the right of 12, and if we add 27, we add it to the right of 27. If we add 16, we add 16 to the left of 20. So what you see here is that if there is no
# child to a node, we have to create a new child, otherwise we keep on going down the tree until we are at the end.
# This also makes is very easy to search for the smallest, and largest, items in a tree, as the item on the far left side will be the smallest, and the item on the far right will be the
# largest.

# Now, what if we wanted to remove a given item from a binary search tree. Let us say that we want to remove a leaf node, which are nodes that do not have any children in them.
# Well we first have to search for this value. We start at the root node, and follow it down the tree. And because it is a leaf node, we just need to notify the parent that the
# given node has been removed. This will set it up for the garbage collector. But what if we wanted to remove a node with a single child? We still need to start at the root node
# and find the item we want to remove. Well, this is pretty simple still, we need to notify the parent node, and point it to the child of the node we want to remove.
# But what if we want to remove a node that contains two children? Maybe we want to remove the root node? This kind of shows you that the number of children that the node
# that we want to remove dictates ultimately the type of problem we have here. Well in this case, we need to look at either the successor, or the predecessor. The smallest item
# to the right of the subtree we call the successor. And we call it the successor, because this is the next item in the natural ordering. So if our head node is 32, and our first child
# node to the right is 55 and to the left our first child node is 10, 55 will be our successor, as it is naturally the value that comes next if we sort the values. Now the predecessor
# is the largest item in the left subtree. So if the last child of our 10 node all the way to the right is 23 (10->19->23) then it is the largest.
# For us, we will deal with our predecessor. We want to swap the item we want to remove. For us, we will swap 23 and 32, and now that 32 is a leaf node, it is easy for us to remove it.
# We call this mathematical reduction. This is when we have a complex problem, and we reduce it to a form of a problem we have previously solved before.
# This is why we want to find the predecessor or successor. After we remove our node with children (head node in our case), we still see that it is a valid binary search tree.
# This is why we used the predecessor, because we need to make sure that this stays a valid binary search tree.

# Now that we know the theory behind inserting and deleting nodes, let us talk about Binary Search Tree Traversal. When we talk about tree traversal, what we are talking about
# is us visiting every node of the binary search tree exactly once in O(N) linear running time. This because we have to consider all of the N items.
# Now there are three traversal methods we want to talk about:
# Pre-Order Traversal. This is were we visit the root node of the binary tree, then the left subtree, and then finally the right subtree is a recursive manner. So we start with our
# left subtree, and within that we use pre-order traversal once again on the left subtree of our left subtree, and we keep doing that. Then we look at the right subtree of the left subtrees.
# And then we do the same of the right subtree of the left subtree, and we just keep doing this until we are done, and then we move onto the right subtree of the root node.

# Post-Order Traversal. This is where we visit the left subtree of the binary tree then the right subtree, and last the root node in a recursive manner.

# In-Order Traversal (Sorted Order). This is the most crucial traversal method. Here we visit the left subtree of the binary tree, then the root node, and finally the right subtree
# in a recursive manner. We have to do this if we need the data in a sorted order.

# So now we want to go ahead and look at the run time complexity of a binary search tree.
# Space Complexity
## Average Case O(N) Worst Case O(N)
# Insertion
## Average Case O(logN) Worst Case O(N)
# Deletion 
## Average Case O(logN) Worst Case O(N)
# Search
## Average Case O(logN) Worst Case O(N)

# This os why we like binary search trees, as it is very consistent. But we can end up with binary search trees that are unbalanced. This is when either the left, or right, subtrees
# can contain many more items than the other subtrees. This leads to a worst case scenario where we can actually be reduced from a logarithmic running time complexity, all the way down
# to a linear running time complexity.

# So I want to implement our binary search tree now.

class Node:
    # So we want to store our data, our left child, and last our right child:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        # Now because we won't be using recursion, we need to store a reference to the parent node as well
        self.parent = parent

# So this node is going to be a vertex, or a node, in the binary tree.

class BinarySearchTree:
    # Now within the init function, we want to create the root node. The root node at the beginning will be initialed to be None
    def __init__(self):
        self.root = None
    def insert(self, data):
        # So we want to insert our new Node, and if our root node is none, much like our head in the linked list, we want to initialize it with a new Node, but
        # we want to have the parent be None.
        if self.root is None:
            self.root = Node(data, None)
        # If our root is not none we want to call our insert_node method, which will insert our node:
        else:
            self.insert_node(data, self.root)
    # So we want to create our method that will actually handle the insertion of our nodes:
    def insert_node(self, data, node):
        # Now remember the basic principle of our tree is that if the given data is smaller than the given node, we go left. If it is greate than the actual node, we go right.
        # So we call our node.data as we are hopping from node to node, until there is no more child.
        if data < node.data:
            # We also want to see if a given node is already present as well.
            # Here we want to check if we already have a left child.
            if node.leftChild is not None: # Or if node.leftChild:
                # We then want to call the function recursively
                self.insert_node(data, node.leftChild)
            # Else we we do not have a left child
            else:
                node.leftChild = Node(data, node)
        # if this isn't the case, we know it has to be greater, so we want to test if there are right subtrees or not:
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
    # Now we want to do our in-order traversal, which will be our sorted order
    def traverse(self):
        # let us first check if the root is none or not.
        if self.root: # or is not None
            self.traverse_in_order(self.root)
    # Now remember that we start on the left subtree, go to the node, and then end with the right subtree.
    def traverse_in_order(self, node):
        # So we want to first check if we have a left child
        if node.leftChild is not None:
            # We want to recursively call this traverse_in_order
            self.traverse_in_order(node.leftChild)
        
        # If it isn't the left child, then we are dealing with the root node, so we want to print it out:
        print('%s' % node.data)

        # Now we want to go ahead and deal with the right child:
        if node.rightChild is not None:
            self.traverse_in_order(node.rightChild)

    # What if we wanted to find the maximum value within our binary tree? How would we go about doing this?
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        # Here we want to get our maximum value. Remember that within our binary tree, the maximum value lives far to the right in the far right subtree.
        if node.rightChild is not None:
            return self.get_max(node.rightChild)

        # If there are no right childs left, we know that this is the farthest right node in the tree.
        return node.data

    # Now let us look at getting the min value as well
    def get_min_value(self):
        if self.root is not None:
            return self.get_min(self.root)
    
    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data



bst = BinarySearchTree()
bst.insert(100)
bst.insert(20)
bst.insert(40)
bst.insert(158)
bst.insert(10)
bst.insert(-4)
bst.insert(204)
bst.insert(168)
bst.insert(3426562324123165674)

bst.traverse()

print("Max item is:", bst.get_max_value())
print("Min item is:", bst.get_min_value())

# We could make use of iteration in here as well, and it may be better, but for now we prefer the compact nature of recursion. So let us look at the iterative approach, not the
# recursive.

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)
    def traverse_in_order(self, node):
        if node.leftChild is not None:
            self.traverse_in_order(node.leftChild)
        print('%s' % node.data)
        if node.rightChild is not None:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        actual = node
        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def get_min_value(self):
        if self.root is not None:
            return self.get_min(self.root)
    
    def get_min(self, node):
        actual = node
        while actual.leftChild is not None:
            actual = actual.leftChild
        
        return actual.data

bst = BinarySearchTree()
bst.insert(100)
bst.insert(20)
bst.insert(40)
bst.insert(158)
bst.insert(10)
bst.insert(-4)
bst.insert(204)
bst.insert(168)
bst.insert(3426562324123165674)

bst.traverse()

print("Max item is:", bst.get_max_value())
print("Min item is:", bst.get_min_value())

# You can choose either, but I personally prefer recursion.