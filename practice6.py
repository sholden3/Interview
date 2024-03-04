# Data Structures

## Linked List

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
    def remove(self):
        if self.head is None:
            raise Exception("LinkedList is empty")
        else:
            self.head = self.head.nextNode
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

## Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prevNode = self.tail
            self.tail.nextNode = newNode
            self.tail = newNode
    def remove(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            self.tail.prevNode.nextNode = None
            self.tail = self.tail.prevNode
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

## Stack

class Stack:
    def __init__(self):
        self.stack = []
    def append(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

## Queue

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

## Queue with Stacks

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self,data):
        self.enqueue_stack.append(data)
    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Queue is empty")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                data = self.enqueue_stack[-1]
                del self.enqueue_stack[-1]
                self.dequeue_stack.append(data)
        data = self.dequeue_stack[-1]
        del  self.dequeue_stack[-1]
        return data

## Queue with Stacks and Recursion

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("Queue is empty")
        if len(self.queue) == 1:
            data = self.queue[-1]
            del self.queue[-1]
            return data
        data = self.queue[-1]
        del self.queue[-1]
        dequeued_data = self.dequeue()
        self.queue.append(data)
        return dequeued_data

# Algorithms Sorts

## Insertion Sort

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and arr[i - 1] > newElement:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = newElement

arr = [1,2,5,3,0,-1,-1,23,4,1]
insertionSort(arr)
print(arr)

## Selection Sort

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

arr = [1,2,5,3,0,-1,-1,23,4,1]
selectionSort(arr)
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
        quickSort(arr, pi+1, high)

arr = [1,2,5,3,0,-1,-1,23,4,1]
quickSort(arr, 0, len(arr) - 1)
print(arr)

# Algorithms Searches

## Binary Search

def binarySearch(arr, low, high, x):
    if len(arr) == 0:
        raise Exception("Array is empty")
    if len(arr) == 1:
        return arr
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, high, x)
    return -1

print(binarySearch(arr, 0, len(arr) - 1, 234))

# Programming Questions Arrays

## Reversing an array in place

def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
reverseArray(arr)
print(arr)

## Reversing an array with extra space allocated

## Return Duplicate Values

def dupValues(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

print(dupValues(arr))

## Print Duplicate Values

## Special case Duplicate Values in positive int array where largest number is no larger then max size of array

def specialDupCase(intArr):
    for i in intArr:
        if intArr[abs(i)] >= 0:
            intArr[abs(i)] = -intArr[abs(i)]
        else:
            print(str(abs(i)), "is a dupe")

arr = [1,2,3,1,2,5,6,4,3,6,7,5]
specialDupCase(arr)

## Remove Duplicates from an Array in Place

def removeDupes(arr):
    if len(arr) == 0:
        raise Exception("Array is empty")
    pi = 0
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i+1]:
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1
    arr[pi] = arr[-1]
    return pi

arr = [1,2,5,3,0,-1,-1,23,4,1]
quickSort(arr, 0, len(arr) - 1)
print(removeDupes(arr))
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

number = 12354521343123123
print(reverseInt(number))

## Reverse a negative integer

## Find the missing number in a given integer array of 1 to 100

def findMissingNum(arr):
    total = 1
    for i in range(2, len(arr) + 2):
        total += i
        total -= arr[i - 2]
    return total

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17]
print(findMissingNum(arr))

## Find multiple missing numbers in a given itneger array of 1 to 100

def findMultMissingNumbers(arr):
    # Initialize an array with zero
    # of size equals to the maximum
    # element in the array
    b = [0] * (arr[-1] + 1)

    # make b[i]=1 if i is present in the array
    for i in range(len(arr)):
        b[arr[i]] = 1
    # print the indices where b[i]=0
    for i in range(arr[0], arr[len(arr) - 1] + 1):
        if b[i] == 0:
            print(i)

arr = [1,4,5,7,8,9,10,12,14]
findMultMissingNumbers(arr)

## Find all pairs in an array of integers whose sum is equal to the given number

def getPairsCount(arr, sum):
    count = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                count += 1
    
    return count

arr = [1,5,7,-1]
sum = 6
print(getPairsCount(arr, sum))

# Programming Questions Strings

## Palindrome

def palindrome(string):
    string = list(string)
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print(palindrome("racecar"))

## Anagram

def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = list(word1)
    word2 = list(word2)
    selectionSort(word1)
    selectionSort(word2)
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            return False
    return True

print(anagram("wes", "sew"))

## Find First Non-Repeating Character in a String

def findFirstNonRepeating(string):
    counts = {}
    order = []
    for i in string:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            order.append(i)
    for i in order:
        if counts[i] == 1:
            return i
    return -1

string = "13fdsfx42342341xr r2r234"
print(findFirstNonRepeating("13fdsfx42342341xr r2r234"))

## Find First Non-Repeating Character in a String using List Comprehension
count = [a for a in string if string.count(a) == 1][0]
print(count)

## Find First Non-Repeating Character in a String using Generator

count = (a for a in string if string.count(a) == 1)
print(next(count))

## Print all permutations of String iterative

## Print all permutations of string recursive

def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1m r)
            a[l], a[i] = a[i], a[l]

## Find longest palindrome in a given string

# Programming Questions Linked Lists

## Check if a linked list contains a cycle, and return the initial node of the cycle if true

## Finding middle node in single linked list

## Finding third node from the end singly linked list

## Reverse a singly Linked List

# Programming Questions Stacks

## Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory