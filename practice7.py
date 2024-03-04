# Data Structures

## Linked List

## Doubly Linked List

## Stack

## Queue

## Queue with Stacks

## Queue with Stacks and Recursion

# Algorithms Sorts

## Insertion Sort

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and arr[i-1] > newElement:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = newElement

arr = [0,34,5,1,23,6,8,-23,-34,1,9]
insertionSort(arr)
print(arr)

## Selection Sort

def selectionSort(arr):
    lastUnsortedIndex = len(arr) - 1
    while lastUnsortedIndex > 0:
        largest = 0
        i = 1
        while i <= lastUnsortedIndex:
            if arr[i] >= arr[largest]:
                largest = i
            i += 1
        arr[largest], arr[lastUnsortedIndex] = arr[lastUnsortedIndex], arr[largest]
        lastUnsortedIndex -= 1

arr = [0,34,5,1,23,6,8,-23,-34,1,9]
insertionSort(arr)
print(arr)

## Quicksort

def partition(arr, low, high):
    pi = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pi:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if len(arr) == 0:
        raise Exception("Array is empty")
    if len(arr) == 1:
        return arr
    if low <= high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)


arr = [0,34,5,1,23,6,8,-23,-34,1,9]
quickSort(arr,0,len(arr)-1)
print(arr)

# Algorithms Searches

## Binary Search

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

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert(self, data):
        self.numOfNodes += 1
        newData = Node(data)
        if self.head is None:
            self.head = newData
        else:
            newData.nextNode = self.head
            self.head = newData

    def remove(self):
        if self.head is None:
            raise Exception("Linked List in None")
        else:
            self.numOfNodes -= 1
            self.head = self.head.nextNode

    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    def insertMid(self, data):
        newNode = Node(data)
        prevNode = None
        currentNode = self.head
        mid = self.numOfNodes // 2
        i = 0
        while i <= mid:
            if i == mid:
                prevNode.nextNode = newNode
                newNode.nextNode = currentNode.nextNode
            prevNode = currentNode
            currentNode = currentNode.nextNode
            i += 1

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(5)
linkedList.insert(3)
linkedList.insert(2)
linkedList.insert(20)
linkedList.traverse()
print("Divide")
linkedList.insertMid(50)
linkedList.traverse()