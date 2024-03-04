# QuickSort

def partition(arr, start, end):
    i = start - 1
    pi = arr[end]

    for j in range(start, end):
        # maintain it as stable if possible
        if arr[j] < pi:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return (i + 1) 

def quickSort(arr, start, end):
    if len(arr) == 1:
        return arr
    if start <= end:
        pi = partition(arr, start, end)
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)

arr = [-2,3,4,-1,0,0,-2,32,4,12]
start = 0
end = len(arr) -1
quickSort(arr, start, end)
print(arr)

# Binary Search

def binarySearch(arr, start, end, x):
    if start <= end:
        pi = (start + end) // 2
        if arr[pi] == x:
            return pi
        if arr[pi] < x:
            return binarySearch(arr, pi + 1, end, x)
        if arr[pi] > x:
            return binarySearch(arr, start, pi - 1, x)
    return -1

print(binarySearch(arr, start, end, 0))
print(binarySearch(arr, start, end, 32))
print(binarySearch(arr, start, end, 12))
print(binarySearch(arr, start, end, -2))

# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def insert(self, data):
        self.numOfNodes += 1

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        self.numOfNodes += 1

        newNode = Node(data)

        currentNode = self.head

        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode
        
    def remove(self, data):
        if self.head is None:
            return

        currentNode = self.head
        prevNode = None
        while currentNode is not None and currentNode.data != data:
            prevNode = currentNode
            currentNode = currentNode.nextNode

        if currentNode is None:
            return
        
        self.numOfNodes -= 1

        if prevNode is None:
            self.head = currentNode.nextNode
        else:
            prevNode.nextNode = currentNode.nextNode

    def removeFirst(self):
        if self.head is None:
            return

        self.head = self.head.nextNode

    def sizeOfList(self):
        return self.numOfNodes

    def traverse(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(-1)
linked_list.insert("test")
linked_list.insert("Wes")
linked_list.traverse()
linked_list.insertEnd("Amanda")
linked_list.traverse()
linked_list.remove(-1)
linked_list.traverse()
linked_list.removeFirst()
linked_list.traverse()

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

    def insert(self, data):
        newNode = Node(data)
        self.numOfNodes += 1

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode

    def removeLast(self):
        if self.head is None:
            return
        self.tail = self.tail.prevNode
        self.tail.nextNode = None
        self.numOfNodes -= 1
    
    def sizeOfList(self):
        return self.numOfNodes

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
doublyLinkedList.insert("Wes")
doublyLinkedList.insert("test")
doublyLinkedList.insert(1)
doublyLinkedList.traverseForward()
doublyLinkedList.insert(2)
doublyLinkedList.traverseForward()
doublyLinkedList.removeLast()
doublyLinkedList.traverseForward()

# Stack

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stackSize() < 1:
            return -1
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data
    
    def stackSize(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]

stack = Stack()

stack.push(5)
stack.push(10)
stack.push(50)
print(stack.stack)
stack.pop()
print(stack.stack)

# Reversing array in-place

def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
arr = [1,3,6,2,1,5]
start = 0
end = len(arr) - 1
reverseArray(arr, start, end)
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

word1 = "catac"
word2 = "wes"

print(palindrome(word1))
print(palindrome(word2))


# Integer Reversion

def intReversion(value):
    reversed = 0
    remainder = 0
    while value > 0:
        remainder = value % 10
        value = value // 10
        reversed = reversed * 10 + remainder
    return reversed

print(intReversion(4324541))
print(intReversion(100))

# Anagram

def partition(arr, start, end):
    i = start - 1
    pi = arr[end]

    for j in range(start, end):
        if arr[j] < pi:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return (i + 1)

def quickSort(arr, start, end):
    if len(arr) <= 1:
        return
    if start <= end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi - 1)
        quickSort(arr, pi + 1, end)

def anagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) != len(word2):
        return False
    start = 0
    end = len(word1)
    quickSort(word1, start, end - 1)
    quickSort(word2, start, end - 1)
    for j in range(0, end):
        if word1[j] != word2[j]:
            return False
    return True

print(anagram("wes","sew"))
print(anagram("wes","west"))
print(anagram("wes","ses"))
    

# Duplicate Values

def duplicateValues(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

arr = [1,5,64,23,1,3,6,4,5,3,4,6,34,9,76,4,5,64]
print(duplicateValues(arr))

def duplicateValues(arr):
    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            print(str(i), "is a duplicate")

duplicateValues(arr)

# if all positive ints, and the largest value is less than or equal to length of array:

def duplicateIntCase(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = -arr[abs(i)]
        else:
            print(str(abs(i)), "is a dup")

arr = [0,4,3,2,1,8,5,6,3,8]
duplicateIntCase(arr)

# Finding middle node in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def insert(self, data):
        self.numOfNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def middleNode(self):
        slowCounter = self.head
        fastCounter = self.head
        while fastCounter.nextNode is not None and fastCounter.nextNode.nextNode:
            fastCounter = fastCounter.nextNode.nextNode
            slowCounter = slowCounter.nextNode
        
        return slowCounter.data

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(50)
linkedList.insert(5)
linkedList.insert(23)

print(linkedList.middleNode())

# Reverse linked list in-place

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

    def insert(self,data):
        self.numOfNodes += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prevNode = self.tail
            self.tail.nextNode = newNode
            self.tail = newNode

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
doublyLinkedList.insert(20)
doublyLinkedList.insert(39)
doublyLinkedList.insert(5)
doublyLinkedList.insert(50)
doublyLinkedList.reverse()
doublyLinkedList.traverse()

# Find first non repeated character from a string

# Remove duplicates from an array in place

# Check if a given linked list contains a cycle. Find the initial node of the cycle.

# Difference between a stable and unstable sorting algorithm

# What is the difference between Comparison and Non-comparison Sorting Algorithms.

# Swap two numbers without using the third variable.

# How to find the missing number in a given integer array of 1 to 100

# How to find the largest and smallest number in an unsorted integer array.

# How do you find all pairs of an an integer array whose sum is equal to a given number

# How are duplicates removed from a given array (Python and Java)

# How are duplicates removed from a given array in place.

# Reverse a signly linked list

# How to find the third node from the end is a signly linked list

# How do you find the sum of two linked lists using Stack.

# Reverse a string using recursion

# Check if a string only contains digits

# Count vowels and consonants is a given string

# Find permutations of a string

# Check if two strings ar a rotation of each other

# Queue

# Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory.

# Queue Implementation with Stacks

# Queue Implementation with a stack and recursion