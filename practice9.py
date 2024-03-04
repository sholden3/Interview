# Data Structures

## Linked List

### A linked list allows for us to get O(1) constant time when adding and retrieving the first element of our data structure
### This is because each of our elements are wrapped in a Node class, which keeps a reference of the next Node class in the list, as well as allowing
### Our data to be non-sequential in nature. This means that we no longer can use random indexing.

### First we want to create our Node class, which will hold all our header information for our linked list:

class Node:
    # This will hold our reference to the data, as well as the next node, which will start as None
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    # Our actual implementation of the data structure
    # We initialize with the size of oru linked list as 0, and the header node, which is our entry node, as None
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
    # There are many different helper methods we can add to this, but we will stick to the main ones for now.
    # We want to allow for us to inserty in a new node at the beginning in O(1) running time:
    def insert(self, data):
        # We first increment the number of nodes by 1
        self.numOfNodes += 1
        # We create our new node
        newNode = Node(data)
        # We check to see if our head is None or not
        if self.head is None:
            # Assign newNode to our head
            self.head = newNode
        else:
            # Otherwise assign the current head to the nextNode
            newNode.nextNode = self.head
            self.numOfNodes += 1
    # We want to be able to remove the first node
    def remove(self):
        # Let us first check to see if the linked list is empty or not
        if self.head is None:
            raise Exception("Linked list does not contain data")
        else:
            self.head = self.head.nextNode
            self.numOfNodes -= 1
    # Now we want to traverse this node
        def traverse(self):
            # Let us keep track of our current node in the method, starting at the head
            currentNode = self.head
            # While the currentNode is not None, traverse through all nodes
            while currentNode is not None:
                print(currentNode.data)
                currentNode = currentNode.nextNode
                # We print out the data of the current node, and then proceed to the next node

## Doubly Linked List
                
### One issue of the singly linked list is that we are only ever albe to move from the head node up. This means that if we wanted to either insert or retireve an element
### At the end of the linked list, we would have to iterate completely through it at O(n) worse case running time.
                
# create our Node class, which now containes a reference to prevNode

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

## Now let us create our linked list class with an optional tail

class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

# Now we want to handle our insert. In particular we want to handle inserting our data at the end.
    def insert(self, data):
        self.numOfNodes += 1
        newNode = Node(data)
        # If head is empty, than so must tail be.
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode
    
    def remove(self):
        if self.head is None:
            raise Exception("Linked list contains no data")
        else:
            self.numOfNodes -= 1
            self.tail = self.tail.prevNode
            self.tail.nextNode = None

    def traverseForwards(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def traverseBackwards(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.prevNode
## Stack

### We use stacks for last in first out (LIFO) operations. This is an abstract data type, not a data structure, as it is built ontop of the list datatype
            
class Stack:
    def __init__(self):
        self.stack = []
    # We want to be able to append to the end of a start at O(1) time complexity. Because it is at the end, we do not have to worry about shifting elements
    def append(self, data):
        self.stack.append(data)
    # We want to be able to pop the values off the end using random indexing
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack contains no data")
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

## Queue
        
### Queues have a firt in first out (FIFO) operations. These are usually used by the OS and multithreading.
### We will implement this with a list, though we could do a linked list
        
class Queue:
    def __init__(self):
        self.queue = []
    # We need an enqueue method which will add the element at the end.
    def enqueue(self, data):
        self.queue.append(data)
    # We need a dequeue method which will take the first element of the array. Though this is O(1) for retrieving the element, it is O(N) for shifting the data.
    # We can get around this by utilizing our linkedlist from before, though now our data will not be sequential in memory.
    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue does not contain data")
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

## Queue with Stacks
        
### If we do not have a memory constraint, one thing we can do is make use of two stacks, one for enqueue, and one for dequeue. This way we can try to get our O(1) time complexity.
        
class Queue:
    def __init__(self):
        self.queue_stack = []
        self.dequeue_stack = []
    # When we enqueue our data, we want to add it to the enqueue stack for O(1)
    def enqueue(self, data):
        self.queue_stack.append(data)
    # Now when we dequeue our stack, we want to first check if our dequeue_stack has any data. If it does, we want to pull from this. If not we want to pop our data from our enqueue stack
    # into this, meaning that at the top of our stack, will be our oldest data, and at the bottom the newest
    def dequeue(self):
        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            raise Exception("Stack does not contain data")
        # If our dequeue stack == 0, we want to populate it from our enqueue stack
        elif len(self.dequeue_stack) == 0:
            # Now we want to loop through queue_stack from top to bottom (newest to oldest), and reverse that for our dequeue_stack and populate it.
            while len(self.queue_stack) > 0:
                # Grab the data from our enqueue stack and append it to our dequeue stack, and then delete it.
                data = self.enqueue_stack[-1]
                self.dequeue_stack.append(data)
                del self.enqueue_stack[-1]
            # Take the data from the end of our dequeue stack and return it. This is the oldest data.
            data = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return data
        else:
            # If dequeue_stack is not empty, that means that we have historical data to take out.
            # As when we populate our dequeue stack we remove all data from our enqueue stack, we do not have to repopulate our dequeue stack until
            # our dequeue stack is empty as well
            data = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return data
                

## Queue with Stacks and Recursion

# Algorithms Sorts

## Insertion Sort
        
### Here we divide the array into two sections, an unsortedPartition and a sortedPartition. This is useful if we do not have a memory constraint
        
def insertionSort(arr):
    # We want to iterate through the first unsorted index, moving up 1 every time. As our array partition at index 0 will always be sorted we startt at 1.
    for firstUnsortedIndex in range(1, len(arr)):
        # We then want to store our item at the firstUnsortedIndex into our newElement variable in order for us to compare.
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        # we are going to check against every item in the sorted section of the index, which is i > 0. We will then check at i - 1 compared to the new ELement, which will be at
        # i to see if the balue is larger than the new element, if so we want to assign the value of arr[i-1] to i, iterating down
        while i > 0 and arr[i - 1] > newElement:
            # if i is not the last index, and i-1 is greater than the current new element, we want to iterate this value up from i - 1 to i. This will continuously
            # move down our list, moving the value up, until we find the spot that our value fits, which we will then assign our new Element.
            arr[i] = arr[i-1]
            i -= 1
        # We then want to assign the value at arr[i] with newElement, as we are done sorting at this iteration
        arr[i] = newElement

## Selection Sort
        
### Selection sort is similar to insertion sort, except we do all the switching at the end. This is useful if we have high memory constraint
        
def selectionSort(arr):
    # Let us get the last index of the array as our last unsorted inded
    lastUnsortedIndex = len(arr) - 1
    # While we are greater than 0, let us iterate down
    while lastUnsortedIndex > 0:
        largest = 0
        i = 1
        while i <= lastUnsortedIndex:
            if arr[i] > arr[largest]:
                largest = i
            i += 1
        arr[largest], arr[lastUnsortedIndex] = arr[lastUnsortedIndex], arr[largest]
        lastUnsortedIndex -= 1

## Quicksort
        
### An O(nlogn) run time complexity making use of recursion
        
def partition(arr, low, high):
    i = low - 1
    pi = arr[high]
    for j in range(low, high):
        if arr[j] < pi:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low <= high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Algorithms Searches

## Binary Search
        
def binarySearch(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, high, x)
        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

# Programming Questions Arrays

## Reversing an array in place

## Reversing an array with extra space allocated

## Return Duplicate Values

## Print Duplicate Values

## Special case Duplicate Values in positive int array where largest number is no larger then max size of array

## Remove Duplicates from an Array in Place

# Programming Questions Integers

## Reverse an integer

## Reverse a negative integer

## Find the missing number in a given integer array of 1 to 100

## Find multiple missing numbers in a given itneger array of 1 to 100

## Find all pairs in an array of integers whose sum is equal to the given number

# Programming Questions Strings

## Palindrome

## Anagram

## Find First Non-Repeating Character in a String

## Find First Non-Repeating Character in a String using List Comprehension

## Find First Non-Repeating Character in a String using Generator

## Print all permutations of String iterative

## Print all permutations of string recursive

## Find longest palindrome in a given string

# Programming Questions Linked Lists

## Check if a linked list contains a cycle, and return the initial node of the cycle if true

## Finding middle node in single linked list

## Finding third node from the end singly linked list

## Reverse a singly Linked List

# Programming Questions Stacks

## Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory