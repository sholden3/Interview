#  QuickSort

## Create the partition, which we will use to divide the unsorted from the sorted, from right to left (largest to smallest).

def partition(arr, low, high):
    i = low - 1
    pi = arr[high]

    for j in range(low, high):
        if arr[j] < pi:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low <= high:
        pi = partition(arr,low,high)
        quickSort(arr,low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [2,-43,123,5,234,1,0,54,54,34,0,-123,432]
low = 0
high = len(arr) - 1
quickSort(arr, low, high)
print(arr)

# SelectionSort

## Useful if already sorted and when memory space is limited, as all swapping is done at end.

def selectionSort(arr):
    lastUnsortedIndex = len(arr) - 1
    while lastUnsortedIndex > 0:
        largest = 0
        i = 1
        while i <= lastUnsortedIndex:
            if arr[i] > arr[largest]:
                largest = i
            i += 1
        arr[largest], arr[lastUnsortedIndex] = arr[lastUnsortedIndex], arr[largest]
        lastUnsortedIndex -= 1


print("Selection Sort start")
arr = [-23, 3, 23, 1, 0, 1, -34, 3, 34]
selectionSort(arr)
print(arr)
print("Selection Sort end")

# InsertionSort

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and arr[i-1] > newElement:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = newElement

# Binary Search

## Divide and conquer algorithm

def binarySearch(arr, low, high, x):
    if low <= high:
        pi = (low + high) // 2
        if arr[pi] == x:
            return pi
        if arr[pi] < x:
            return binarySearch(arr, pi + 1, high, x)
        if arr[pi] > x:
            return binarySearch(arr, low, pi - 1, x)

def partition(arr, low, high):
    i = low - 1
    pi = arr[high]

    for j in range(low, high):
        if arr[j] < pi:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low <= high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [23,43,1,-2,43,-313,545,324,1]
low = 0
high = len(arr) - 1
quickSort(arr, low, high)
print(arr)
print(binarySearch(arr, low, high, 545))

# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def addNode(self, data):
        self.numOfNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self):
        if self.head is None:
            return
        self.numOfNodes -= 1
        self.head = self.head.nextNode

    def traverse(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

linkedList = LinkedList()
linkedList.addNode(10)
linkedList.addNode(23)
linkedList.addNode("ten")
linkedList.traverse()
linkedList.remove()
linkedList.traverse()

# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)
        self.numOfNodes += 1
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode

    def remove(self):
        if self.tail is None:
            return
        self.tail = self.tail.prevNode
        self.tail.nextNode = None
        self.numOfNodes -= 1

    def traverseForward(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def traverseBackward(self):
        currentNode = self.tail
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.prevNode

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.addNode(1023)
doublyLinkedList.addNode(343)
doublyLinkedList.addNode(4342452)
doublyLinkedList.traverseForward()
doublyLinkedList.traverseBackward()

# Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return -1
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

stack = Stack()
stack.push(10)
stack.push(34)
stack.push(3)
stack.push(23)
print(stack.stack)
stack.pop()
print(stack.stack)
print(stack.peek())
print(stack.stack)

# Reversing an array in place

def arrayReverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -=1

arr = [-23, 43, 0, 343,-233, 54]
arrayReverse(arr)
print(arr)

# Palindrome

def palindrome(word):
    word = list(word)
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

word1 = "wes"
word2 = "wew"

print(palindrome(word1))
print(palindrome(word2))

# Integer Reversion

def intReversion(value):
    remainder = 0
    reversed = 0
    while value > 0:
        remainder = value % 10
        value = value // 10
        reversed = reversed * 10 + remainder
    return reversed

value = 231053405
print(intReversion(value))

# Anagram

# using insertion sort for this one

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and arr[i - 1] > newElement:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = newElement 

def anagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) != len(word2):
        return False
    insertionSort(word1)
    insertionSort(word2)

    for j in range(0, len(word1)):
        if word1[j] != word2[j]:
            return False
    return True

print(anagram("test","test"))
print(anagram("test","tset"))

print(anagram("test","tesst"))

# Duplicate Values Return Dict

def duplicates(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

arr = [23,4,54,1,2,-2,-1,0,23,78,8,45,3]
print(duplicates(arr))

# Duplicate values print

def duplicates(arr):
    dict={}
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            print(str(i), "is a duplicate")

arr = [1,43,6,34,1,3,0,-34,-1,-3,-1,0]
duplicates(arr)

# If all values are positive ints with a max size less than or equal to length of an array

def duplicateInt(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = -arr[abs(i)]
        else:
            print(str(abs(i)), "is a dup")

arr = [1,3,2,5,1,5,4,9,8,7,6]
duplicateInt(arr)

# Finding middle node in single linked, or doubly linked, list

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self):
        if self.head is None:
            return -1
        self.head = self.head.nextNode

    def traverse(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def middleNode(self):
        slowCounter = self.head
        fastCounter = self.head

        while fastCounter.nextNode is not None and fastCounter.nextNode.nextNode:
            fastCounter = fastCounter.nextNode.nextNode
            slowCounter = slowCounter.nextNode
        
        return slowCounter.data

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(5)
linkedList.insert("3")
linkedList.insert(34)
linkedList.insert("test")
linkedList.traverse()
print("middleNode:",linkedList.middleNode())
linkedList.remove()
linkedList.remove()
linkedList.traverse()
print("middleNode:",linkedList.middleNode())
linkedList.remove()
linkedList.traverse()
print("middleNode:",linkedList.middleNode())

class Node:
    def __init__(self, data):
        self.data = data
        self.prevNode = None
        self.nextNode = None

class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode

        self.numOfNodes += 1

    def reverse(self):
        currNode = self.head
        prevNode = None
        nextNode = None
        while currNode is not None:
            nextNode = currNode.nextNode
            currNode.nextNode = prevNode
            prevNode = currNode
            currNode = nextNode

        self.head = prevNode

    def traverse(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.nextNode


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insert(10)
doublyLinkedList.insert(5)
doublyLinkedList.insert(22)
doublyLinkedList.insert(1)
doublyLinkedList.insert(30)
doublyLinkedList.insert(2)
doublyLinkedList.traverse()
doublyLinkedList.reverse()
doublyLinkedList.traverse()

# Queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
queue.dequeue()
print(queue.queue)

# Find first non repeating character in a string

## here we make use of list comprehension. We can also make use of a generator as well

string = 'sfrewrqqqefdsfasdwegrwt'
count = [a for a in string if string.count(a) == 1]
print(count)

# or 

count = [a for a in string if string.count(a) == 1][0]
print(count)

# or as a genrator

count = (a for a in string if string.count(a) == 1)
print(next(count))

# Without using builtins or comprehensions

def findUnique(string):
    order = []
    counts = {}
    for x in string:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            order.append(x)
    for x in order:
        if counts[x] == 1:
            return x
    return None

string = "34234rtegfdasfawfawdsfsd2342341321dfsgsdfagsag"
print(findUnique(string))

# Remove duplicates from an array in place

## SelectionSort

def selectionSort(arr):
    lastUnsortedIndex = len(arr) - 1
    while lastUnsortedIndex > 0:
        largest = 0
        i = 1
        while i <= lastUnsortedIndex:
            if arr[i] > arr[largest]:
                largest = i
            i += 1
        arr[lastUnsortedIndex], arr[largest] = arr[largest], arr[lastUnsortedIndex]
        lastUnsortedIndex -= 1

def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n

    j = 0
    
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j+=1
    arr[j] = arr[n-1]
    j += 1
    return j

arr = [23,4,21,0,-1,2,-32,43,56,0,1,4,2,21,-32]
selectionSort(arr)
print(arr)
print(removeDuplicates(arr, len(arr)))
print(arr)

# Check if a given linked list contains a cycle. Find the initial node of the cycle.

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def push(self,data):
        self.numOfNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def detectCycle(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.nextNode
        return False

linkedList = LinkedList()
linkedList.push(20)
linkedList.push(5)
linkedList.push(23)
linkedList.push(10)

print(linkedList.detectCycle())

linkedList.head.nextNode.nextNode.nextNode.nextNode = linkedList.head

print(linkedList.detectCycle())

# How to find the missing number in a given integer array of 1 to 100

def getMissingNo(arr, n):
    i, total = 0, 1
    for i in range(2, n + 2):
        total += i
        total -= arr[i-2]
    return total

arr = [1,2,4,5,6,7,8]
print(getMissingNo(arr, len(arr)))

# Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory.

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.stack) == 1:
            self.max_stack.append(data)
        elif self.max_stack[-1] <= data:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if len(self.stack) > 0:
            del self.max_stack[-1]
            data = self.stack[-1]
            del self.stack[-1]
            return data
        else:
            return -1

    def get_max_item(self):
        data = self.max_stack[-1]
        del self.max_stack[-1]
        return data

stack = Stack()
stack.push(2)
stack.push(10)
stack.push(3)
stack.push(-1)
stack.push(3)

print(stack.stack)
print(stack.max_stack)
print(stack.get_max_item())
print(stack.pop())
print(stack.stack)
print(stack.max_stack)
print(stack.get_max_item())


# Queue Implementation with stacks

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.dequeue_stack) == 0 and len(self.enqueue_stack) == 0:
            raise Exception("Stacks are empty")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

queue = Queue()
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(6)
print(queue.enqueue_stack)
print(queue.dequeue_stack)
print(queue.dequeue())
print(queue.enqueue_stack)
print(queue.dequeue_stack)