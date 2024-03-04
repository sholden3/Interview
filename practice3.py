# Data Structures

## Linked List

### A linked list allows for us to get O(1) constant time when adding and retrieving the first element of our data structure.
### This is because each of our elements are wrapped in a Node class, which keeps a reference of the next Node class in the list, as well as allowing
### our data to be non-sequential in nature. This means that we no longer can use random indexing.

### First, let us create our Node class, which will hold the header information for our Linked List

class Node:
    # This will hold our reference to the data, as well as the next node, which will start as None.
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    # Our actual implementation of the data structure.
    # We initialize with the size of our linked list as 0, and the header node, which is our entry node, as None
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
    # There are many different helper methods we can add to this, but we will stick to the main ones for now.
    # We want to allow for us to insert in a new node at the beginning in O(1) running time:
    def insert(self, data):
        # We iterate our numOfNodes by 1
        self.numOfNodes += 1
        # We create our new node
        newNode = Node(data)
        # We check to see if our linkedlist is empty
        if self.head is None:
            # If empty, set self.head to newNode
            self.head = newNode
        else:
            # Otherwise, assign the current head to the nextNode of our newNode
            newNode.nextNode = self.head
            # Assign newNode to our head
            self.head = newNode
    # Now, we want to be able to remove the first node
    def remove(self):
        # let us first check to see if the linked list is empty or not
        if self.head is None:
            raise Exception("Linked List does not contain data")
        # If the head is not None, let us go ahead and dereference the head, and assign the value of nextNode as the new head
        else:
            self.numOfNodes -= 1
            self.head = self.head.nextNode
    # Now we want to create our code for use to traverse through our linked list
    def traverse(self):
        # let us keep track of our current node in the method, which will start off at the head
        currentNode = self.head
        # while the currentNode is not None, we want to loop through it:
        while currentNode is not None:
            # Let us print out the data inside the node
            print(currentNode.data)
            # Let us assign currentNode to the next node
            currentNode = currentNode.nextNode

print("Singly Linked List Implementation")
linkedList = LinkedList()
linkedList.insert("10")
linkedList.insert(5)
linkedList.insert(2)
linkedList.insert(20)
linkedList.insert(6)
print("Traversing Singly Linked List")
linkedList.traverse()
linkedList.remove()
print("Traversing Singly Linked List")
linkedList.traverse()

## Doubly Linked List

### One issue of the Singly Linked List, is that we are only ever able to move from the head node up. This means that if we wanted to either insert or retrieve an element
### at the end of the linked list, we would have to iterate completely through it at O(N) worse case running time. Now we still want to utilize the linked list, due to 
### the linked list solving the issue of holes that we run into in an array, so that is where the doubly linked list comes into play, as it allows us to store both
### a head and foot node. When dealing with a doubly linked list, you typically insert at the foot, and traverse from the head.

### We create our node class that will contain our nextNode, prevNode, and data
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None
    
### Now let us create our implementation of the doubly linked list data structure
class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None
    # We want to insert our data at the end here.
    def insert(self,data):
        self.numOfNodes += 1
        newNode = Node(data)
        # If head is empty, than tail must be too. Add the newNode to both
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        # Else there is already data in the linked list. We now add newNode to the end.
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode
    # We want to dereference the tail node as well
    def remove(self):
        if self.head is None:
            raise Exception("The linked list is empty")
        else:
            self.numOfNodes -= 1
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
    # We want to be able to traverse it going forward
    def traverseForwards(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode
    # We also want to be able to traverse backwards as well
    def traverseBackwards(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.prevNode

print("Doubly Linked List Implementation")
doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insert(10)
doublyLinkedList.insert(2)
doublyLinkedList.insert("a")
doublyLinkedList.insert(342.03)
doublyLinkedList.insert("Test Again")
doublyLinkedList.insert([34,43,1,23,6,5,34])
print("Doubly Linked List forwards traverse")
doublyLinkedList.traverseForwards()
print("Doubly Linked List backwards traverse")
doublyLinkedList.remove()
doublyLinkedList.remove()
doublyLinkedList.traverseBackwards()

## Stack

### We use the stack for LIFO operations. This is an abstract data type, not a data structure, as it is built ontop of the list type

class Stack:
    def __init__(self):
        self.stack = []
    # We want to be able to append to the send of a stack, at ordo(1) time complexity. Because it is at the end, we do not need to worry about shifting elements.
    def append(self,data):
        self.stack.append(data)
    # We want to be able to pop the values off the end using random indexing
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("No data in stack")
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

print("Running Stack implementation")
stack = Stack()
stack.append(10)
stack.append(5)
stack.append(50)
stack.append("a")
print("Printing Stack")
print(stack.stack)
print("Popping element from stack:", stack.pop())
print("Popping element from stack:", stack.pop())
print("Printing stack")
print(stack.stack)

## Queue

### Queues have a FIFO, and are usually utilized with multithreading and OS.
### We will implement ours with lists, though we could use linked lists

class Queue:
    def __init__(self):
        self.queue = []
    # We need an enqueue method which will add the element at the end 
    def enqueue(self,data):
        self.queue.append(data)
    # We need a dequeue method which will take the first element out of the array. Though this is O(1) for retrieving the element, it is O(N) for shifting the data.
    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("There is no data in the queue")
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

## Queue with Stacks (REVIEW)

### If we do not have a memory constraint, one thing we can do is make use of two stacks, one for enqueue, and one for dequeue. This way we can try to get our O(1) time complexity

class Queue: 
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    # When we enqueue our data, we want to add it to the enqueue stack. Pretty simple. This is ordo 1 time complexity
    def enqueue(self,data):
        self.enqueue_stack.append(data)
    # Now when we dequeue our stack, we want to first check if our dequeue_stack has data, if it does, we want to pull from this, if not we want to pop our data from our enqueue
    # stack into this, meaning that at the top of our stack will be our oldest data, and at the bottom the newest.
    def dequeue(self):
        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            raise Exception("Queue is empty")
        elif len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                data = self.enqueue_stack[-1]
                self.dequeue_stack.append(data)
                del self.enqueue_stack[-1]
            data = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return data
        else:
            data = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return data

print("Implementation of Queue with stacks")
queue = Queue()
queue.enqueue(10)
queue.enqueue("123")
queue.enqueue(40)
queue.enqueue(29)
print("Printing queue with stacks")
print(queue.enqueue_stack)
print(queue.dequeue_stack)
print("dequeue from stack:", queue.dequeue())
print("dequeue from stack:", queue.dequeue())
print("Printing queue with stacks")
print(queue.enqueue_stack)
print(queue.dequeue_stack)

## Queue with Stacks and Recursions (REVIEW)

### Here we want to do the same thing, but with just one stack, making use of recursion instead
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        # We want to first check if the queue is 0, if so we want to raise an error
        if len(self.queue) == 0:
            raise Exception("No data in queue")
        # We now want to establish our base case, which if our queue len equals 1, we want to return the data
        if len(self.queue) == 1:
            data = self.queue[-1]
            del self.queue[-1]
            return data
        
        # Else we want to keep on popping out the data, and calling dequeue
        # Here we grab the value from the queue and store it in a data variable.
        data = self.queue[-1]
        # We then delete the data afterwards, as we will be adding it back in reverse order
        del self.queue[-1]

        # We now want to call dequeue(). We call dequeue here because we will recusively keep calling it before we append our data back to our queue, and then we will
        # start solving these bottom up, so the last item popped out, will be the last put in.
        # So if we have an array of 30, 20, 5 and 5 is the last popped out, then 5 will be the first of our array back in, but 30 won't be in our arary,
        # as we don't add it back into the queue. Instead we simply return the data in our base case.
        dequeued_data = self.dequeue()
        self.queue.append(data)

        return dequeued_data

print("Implementation of Queue with recursion")
queue = Queue()
queue.enqueue(10)
queue.enqueue("123")
queue.enqueue(40)
queue.enqueue(29)
print("Printing queue with recursion")
print(queue.queue)
print("dequeue from stack:", queue.dequeue())
print("dequeue from stack:", queue.dequeue())
print("Printing queue with recursion")
print(queue.queue)

# Algorithms Sorts

## Insertion Sort (REVIEW)

### Here we divide the array into two sections, an unsortedPartition, and a sortedPartition

def insertionSort(arr):
    # We want to iterate through the First Unsorted Index, moving up one every time. As our array parition at index 0 will always be sorted, we start at 1.
    for firstUnsortedIndex in range(1,len(arr)):
        # We then want to store our item at the firstUnsortedIndex into our newElement variable in order for us to compare.
        newElement = arr[firstUnsortedIndex]
        # We now want to set our i to our firstUnsortedIndex, as we will be using this to compare each item.
        i = firstUnsortedIndex
        # We are going to check against every item in the Sorted section of the index, which is i > 0. We will then check at i - 1 compared to the newELement, which will be at
        # i to see if the value is larger than new Element, if so we want to assign the value of arr[i-1] to i, iterating down
        while i > 0 and arr[i-1] > newElement:
            arr[i] = arr[i-1]
            i -= 1
        # We then want to assign the value at arr[i] with newElement, as we are done sorting at this iteration
        arr[i] = newElement

print("Implementing Insertion Sort")
arr = [23,4,12,675,4,-343,24]
insertionSort(arr)
print(arr)
        
## Selection Sort (REVIEW)

### Selection sort is similar to insertion sort, except we do all switching at the end. This is useful if we have high memory constraint

def selectionSort(arr):
    # Let us get the last index of the array as our last unsorted index
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

print("Implementing Selection Sort")
arr = [1,3,5,1,23,564,6,9,-3,0,-3]
selectionSort(arr)
print(arr)

## Quicksort (REVIEW)

### An O(NlogN) run time complexity, making use of recursion.

### We first need to create our partition method
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

arr = [12,43,6,23,1,3,7,68,-34,3]
quickSort(arr,0,len(arr) - 1)
print("Implementation of quicksort")
print(arr)

# Algorithms Searches

## Binary Search (REVIEW)

def binarySearch(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, high, x)
        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

arr = [-23,-3,0,5,6,78,123,546,3432]
print("Implementing BinarySearch")
print(binarySearch(arr,0,len(arr)-1,-23))

# Programming Questions Arrays

## Reversing an array in place

def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [23,5,342,0,-23,-4,23,542]
reverseArray(arr)
print("Implementing reverse array")
print(arr)

## Reversing an array with extra space allocated

arr = [23,43,1,65,90,0,34,23,1,-34]
arr = arr[::-1]
print("Reversing an array with extra memory")
print(arr)

## Return Duplicate Values

def duplicateValues(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

arr = [23,4,1,23,5,6,6876,45,34,5,3,2,4,6,-34,-54,-3,-2,-2,-434,0]
print("Return duplicate values in dict")
print(duplicateValues(arr))

## Print Duplicate Values

def printDuplicateValues(arr):
    dict = {}
    for i in arr:
        if i in dict:
            print(i)
        else:
            dict[i] = 1

arr = [23,54,2,1,0,34,-434,1,2,4]
print("Print Duplicate Values")
printDuplicateValues(arr)

## Special case Duplicate Values in positive int array where largest number is no larger then max size of array (Review)

def specialIntCase(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = -arr[abs(i)]
        else:
            print(str(abs(i)), "is a dup")

arr = [2,3,6,4,3,1,0,7,5,5]
print("Special case int dups")
specialIntCase(arr)

## Remove Duplicates from an Array in Place (REVIEW)

def removeDuplicatesInPlace(arr, n):
    # We check if n equals 0 or 1, which we will just return n, the size of the list.
    if n == 0 or n == 1:
        return n
    
    # If our array is larger than 1, then we want to loop through it. Remember that this needs to be sorted.
    # j will be our first index.
    j = 0
    # We will also loop through the whole array, except for the last index.
    for i in range(0, n-1):
        # We will check if the value at this place equals the value at one up
        if arr[i] != arr[i + 1]:
            # If they do not equal each other, swap j and i.
            arr[j] = arr[i]
            # increment j up one
            j += 1
            # Much like with our quicksort, if our values do match, we will start lagging j, which will allow us to start shifting all dups to the end.
    # We then want to switch the value at the end of the array to where our partition is.
    arr[j] = arr[n-1]
    # We return our partition
    return j

arr = [2,4,4,4,5,6,8,9,100,233,233,233454,233454]
print("removeDuplicatesInPlace")
print("Partition Index:",removeDuplicatesInPlace(arr, len(arr)))
print(arr)

# Programming Questions Integers

## Reverse an integer

def reverseInt(number):
    remainder = 0
    reversed = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        reversed = reversed * 10 + remainder
    return reversed

number = 2315455
print("Reverse Positive int")
print(reverseInt(number))

## Find the missing number in a given integer array of 1 to 100 (REVIEW)

def getMissingNo(arr):
    n = len(arr)
    # Create a variable for total here, it will equal to 1 for now.
    total = 1
    # We will loop going from 2 to n + 2
    for i in range(2, n + 2):
        # First we add the value of the current index to total
        total += i
        # we will subtract from total the value in arr at i - 2, which will start with index 0
        total -= arr[i-2]
    # return the total
    return total

arr = [1,2,3,4,6,7,8]
print("Get Missing No")
print(getMissingNo(arr))

# Programming Questions Strings

## Palindrome

### Palindrom is a string that matches forwards and backwards

def palindrome(word):
    word = list(word)
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

print("Palindrome Check")
print(palindrome("racecar"))
print(palindrome("test"))

## Anagram

### Check if a word exists in another word

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

def anagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) == len(word2):
        quickSort(word1, 0, len(word1)-1)
        quickSort(word2, 0, len(word2)-1)
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                return False
        return True
    return False

print("Implementing Anagram")
print(anagram("test","tests"))
print(anagram("test","etst"))
print(anagram("test","tess"))

## Find First Non-Repeating Character in a String (REVIEW)

def findFirstUnique(string):
    order = []
    counts = {}
    for i in string:
        if i in counts:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
            order.append(i)
    for i in order:
        if counts[i] == 1:
            return i
    return None

string = "2342143241823912djfhsdjhfjkashfjsadhgfjhwujhewuihfuashfuisahfas"
print("Find first unique in string")
print(findFirstUnique(string))

## Find First Non-Repeating Character in a String using List Comprehension (REVIEW)

unique = [a for a in string if string.count(a) == 1][0]
print("Unique with list comprehension")
print(unique)

## Find First Non-Repeating Character in a String using Generator (REVIEW)

unique = (a for a in string if string.count(a) == 1)
print("Unique with generator")
print(next(unique))

# Programming Questions Linked Lists

## Check if a linked list contains a cycle, and return the initial node of the cycle if true

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
    def insert(self,data):
        self.numOfNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def isCycle(self):
        s = set()
        currentNode = self.head
        while currentNode is not None:
            if currentNode in s:
                return True
            else:
                s.add(currentNode)
                currentNode = currentNode.nextNode
        return False

## Finding middle node in single linked list (REVIEW)

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def middleNode(self):
        fastCounter = self.head
        slowCounter = self.head
        while fastCounter is not None and fastCounter.nextNode.nextNode is not None:
            fastCounter = fastCounter.nextNode.nextNode
            slowCounter = slowCounter.nextNode
        return slowCounter.data

# Programming Questions Stacks

## Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory (REVIEW)

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    def append(self,data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.