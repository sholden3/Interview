import time

class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.NumOfNodes = 0
    def insert(self, data):
        newNode = NodeSingle(data)
        self.NumOfNodes += 1

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # Typically with doubly linked lists, the insert function will
    # insert at the end. So we have to manipulate the tail node in O(1).
    def insert(self, data):
        new_node = Node(data)

        # When the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # There is atleast one item in linked list
        # We keep inserting items at the end
        else:
            self.tail.nextNode = new_node
            new_node.prevNode = self.tail
            self.tail = new_node

    # Remember that one of the huge advantages of doubly linked lists is that
    # we can traverse forwards and backwards.
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.nextNode
    
    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.prevNode

if __name__ == '__main__':
    # linkedList = DoublyLinkedList()
    # linkedList.insert(34)
    # linkedList.insert(54)
    # linkedList.insert(2)

    # linkedList.traverse_forward()
    # linkedList.traverse_backward()

    # So now that we have our doubly linked list, let us compare the running time to our arrays. Remember that in Python
    # our arrays are very similar to arrays in other languages, but we hold references because everything in python is an object.

    # First let us test inserting at the beginning.
    # linkedList = LinkedList()

    # now = time.time()

    # for i in range(500000):
    #     linkedList.insert(i)

    # print("Inserting items into Linked List in %ss" % str(time.time() - now))

    # array = []
    # now = time.time()
    
    # for i in range(500000):
    #     array.insert(0,i)

    # print("Inserting items into Array in %ss" % str(time.time() - now))

    # For my run for 5oo thousand items is:
    # Inserting items into Linked List in 0.8435626029968262s
    # Inserting items into Array in 64.51920652389526s

    # So we see that having O(N) run time dealing with holes and shifting in arrays really eats up our time complexity, while the memory complexity needed
    # for our linkedlist O(1) first item insert is very small in comparison.

    ##### Finding the middle node in a linked list in place without extra memory.

    ## To methods:
    ## 1. Naive Method. We iterate through the list and acount how many elements there are in total.
    ## Traverse the list again and the node with index count // 2 is the middle node.
    ## Though it still has O(N), we have to iterate through the list twice.
    ## 2. Using two pointers. We can use two pointers to get the middle node in O(N).
    ## First pointer: traverse the linked list one node at a time.
    ## Second pointer: travers the linked list two nodes at a time.
    ## When the fast pointer reached the end of the list then the slower pointer is pointing to the middle node.
    ## This is also O(N), but we run through the list once.

    # So for memory sake, let us create our linked list class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.nextNode = None

    class LinkedList:
        def __init__(self):
            self.head = None
            self.numOfNodes = 0

        def insert(self, data):
            newNode = Node(data)
            self.numOfNodes += 1
            if self.head is None:
                self.head = newNode
            else:
                newNode.nextNode = self.head
                self.head = newNode
        
        # This gives us that O(N) single loop running algorithm. This is because by the time we get to the end of the linkedlist,
        # because the fast pointer is double the slow, the slow will always be at the half way point.
        def get_middle_node(self):
            slow_pointer = self.head
            fast_pointer = self.head

            while fast_pointer.nextNode is not None and fast_pointer.nextNode.nextNode:
                fast_pointer = fast_pointer.nextNode.nextNode
                slow_pointer = slow_pointer.nextNode
            
            return slow_pointer.data
    linkedList = LinkedList()

    for i in range(100):
        linkedList.insert(i)

    print(linkedList.get_middle_node())


##### Reverse a linked list in-place
# We have two solutions that we can follow to do this:
# 1. Naive solution. We can consider all the nodes one by one then construct another linked list in reverse order
# The issue here is that it is not in place.
# 2. using pointers we can use pointers to get our reversed linked list in place.
# Both of these do have O(N) running time though.

    class Node:
        def __init__(self, data):
            self.data = data
            self.nextNode = None
            self.prevNode = None

    class doublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            self.numOfNodes = 0

        def insert(self, data):
            newNode = Node(data)
            self.numOfNodes += 1

            if self.tail is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.nextNode = newNode
                self.tail = newNode
    
        # Need to go through this until I understand.
        def reverse(self):
            # This is our current node that we will use to keep track of where we are
            currNode = self.head
            # This is our previous node
            prevNode = None
            # This is our next node
            nextNode = None
            # We want to continue until our node is None. This means we iterated through the entire linked list.
            # 1
            # None
            # 0
            # 1

            # 2
            # 0
            
            while currNode is not None:
                # Set our next node to our currNodes nest node.
                # We want to do this because we will iterate to this node next.
                nextNode = currNode.nextNode
                # We then want to set our currNodes next node to the previous one.
                currNode.nextNode = prevNode
                # Once we do this, we want to swap the previous node with the current node
                prevNode = currNode
                # Last, we want to switch our currNode with the nextNode
                currNode = nextNode
            # We want to set our head to the prevNode.
            self.head = prevNode

        def traverse(self):
            currNode = self.head
            while currNode is not None:
                print(currNode.data)
                currNode = currNode.nextNode
                
    linkedList = doublyLinkedList()

    for i in range(10):
        linkedList.insert(i)

    linkedList.reverse()
    
    linkedList.traverse()
