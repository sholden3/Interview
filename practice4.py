# Data Structures

## Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def remove(self):
        if self.head is None:
            raise Exception("LinkedList is empty")
        data = self.head.data
        self.head = self.head.nextNode
        return data
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

print("Linked List")
linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(20)
linkedList.insert("a")
linkedList.insert("1231")
print("Linked List Traverse")
linkedList.traverse()
print(linkedList.remove())
linkedList.remove()
print("Linked List Traverse")
linkedList.traverse()

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
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = newNode
    def remove(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        data = self.tail.data
        self.tail.prevNode.nextNode = None
        self.tail = self.tail.prevNode
        return data
    def traverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode
        
doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insert(10)
doublyLinkedList.insert(1)
doublyLinkedList.insert("ten")
doublyLinkedList.insert("sddfa")
print("Double Linked List Implementation")
print("Traversing Linked List")
doublyLinkedList.traverse()
print(doublyLinkedList.remove())
print("Traversing Linked List")
doublyLinkedList.traverse()

## Stack

class Stack:
    def __init__(self):
        self.stack = []
    def append(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
print("Stack Implementation")
stack = Stack()
stack.append(10)
stack.append(50)
stack.append(10023)
stack.append(3)
print(stack.stack)
print(stack.pop())
print(stack.pop())
print(stack.stack)

## Queue

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("No data in queue")
        data = self.queue[0]
        del self.queue[0]
        return data

print("Queue implementation")
queue = Queue()
queue.enqueue(13)
queue.enqueue(4)
queue.enqueue("dfsd")
queue.enqueue(434)
queue.enqueue(2)
print(queue.queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.queue)

## Queue with Stacks

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self, data):
        self.enqueue_stack.append(data)
    def dequeue(self):
        if len(self.enqueue_stack ) == 0 and len(self.dequeue_stack ) == 0:
            raise Exception("Queue has no data")
        if len(self.dequeue_stack ) == 0:
            while len(self.enqueue_stack ) > 0:
                data = self.enqueue_stack [-1]
                del self.enqueue_stack [-1]
                self.dequeue_stack .append(data)
        data = self.dequeue_stack [-1]
        del self.dequeue_stack [-1]
        return data

print("Queue implementation Stacks")
queue = Queue()
queue.enqueue(13)
queue.enqueue(4)
queue.enqueue("dfsd")
queue.enqueue(434)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())

## Queue with Stacks and Recursions

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

print("Queue implementation Recursion")
queue = Queue()
queue.enqueue(13)
queue.enqueue(4)
queue.enqueue("dfsd")
queue.enqueue(434)
queue.enqueue(2)
print(queue.queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.queue)

# Algorithms Sorts

## Insertion Sort

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        element = arr[firstUnsortedIndex]
        pi = firstUnsortedIndex
        while pi > 0 and arr[pi-1] > element:
            arr[pi] = arr[pi - 1]
            pi -= 1
        arr[pi] = element

print("Insertion Sort Implementation")
arr = [2,43,2.323,-1,0,23,4,0,11331,23,-232,-1]
insertionSort(arr)
print(arr)

## Selection Sort

def selectionSort(arr):
    lastUnsortedIndex = len(arr) - 1
    while lastUnsortedIndex > 0:
        largest = 0
        pi = 1
        while pi <= lastUnsortedIndex:
            if arr[pi] > arr[largest]:
                largest = pi
            pi += 1
        arr[largest], arr[lastUnsortedIndex] = arr[lastUnsortedIndex], arr[largest]
        lastUnsortedIndex -= 1

print("Selection Sort Implementation")
arr = [2,43,2.323,-1,0,23,4,0,11331,23,-232,-1]
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
    arr[high], arr[i] = arr[i], arr[high]
    return i

def quickSort(arr, low, high):
    if len(arr) == 0:
        raise Exception("Array is empty")
    if len(arr) == 1:
        return arr
    if low <= high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    
print("Quick Sort Implementation")
arr = [2,43,2.323,-1,0,23,4,0,11331,23,-232,-1]
quickSort(arr,0,len(arr)-1)
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
    return None

print("Binary Search Implementation")
print(binarySearch(arr,0,len(arr)-1,11331))

# Programming Questions Arrays

## Reversing an array in place

def reverseArrayInPlace(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

print("Reversing array in place Implementation")
reverseArrayInPlace(arr)
print(arr)

## Reversing an array with extra space allocated

def reverseArrayWithSpace(arr):
    arr = arr[::-1]
    return arr

print("Reversing array with extra space")
arr = reverseArrayWithSpace(arr)
print(arr)

## Return Duplicate Values

def returnDupValues(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

print("Return dict of dup values")
print(returnDupValues(arr))

## Print Duplicate Values

def printDupValues(arr):
    counts = {}
    for i in arr:
        if i in counts:
            print(i,"is a duplicate")
        else:
            counts[i] = 1

print("Print dict of dup values")
printDupValues(arr)

## Special case Duplicate Values in positive int array where largest number is no larger then max size of array

def specialIntCaseDupe(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = -arr[abs(i)]
        else:
            print(str(abs(i)), "is a dupe")

arr = [1,4,3,2,6,8,5,3,2,3,9,0]
print("Special int array")
specialIntCaseDupe(arr)

## Remove Duplicates from an Array in Place

def removeDupesInArray(arr):
    if len(arr) == 0:
        raise Exception("Array is empty")
    if len(arr) == 0:
        return len(arr) - 1
    i = 0
    for j in range(0, len(arr) - 1):
        if arr[j] != arr[j + 1]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i] = arr[-1]
    return i

print("removeDupesInArray Implementation")
arr = [2,43,2.323,-1,0,23,4,0,11331,23,-232,-1]
quickSort(arr,0,len(arr)-1)
print(removeDupesInArray(arr))
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

print("Reverse Number Implementation")
print(reverseInt(231303409988900023480123))

## Reverse a negative integer

## Find the missing number in a given integer array of 1 to 100

def findMissingInSpecialIntArray(arr):
    total = 1
    for i in range(2, len(arr) + 2):
        total += i
        total -= arr[i - 2]
    return total

print("Special case int array 1 to 100")
arr = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18]
print(findMissingInSpecialIntArray(arr))

# Programming Questions Strings

## Palindrome

def findPalindrome(string):
    string = list(string)
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

print("findPalindrome Implementation")
print(findPalindrome("wes"))
print(findPalindrome("ses"))
print(findPalindrome("wess"))
print(findPalindrome("sees"))

## Anagram

def findAnagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) == len(word2):
        quickSort(word1, 0, len(word1) - 1)
        quickSort(word2, 0, len(word2) - 1)
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                return False
        return True
    return False

print("findAnagram implementation")
print(findAnagram("wes", "tes"))
print(findAnagram("wes", "wse"))
print(findAnagram("wees", "tees"))
print(findAnagram("wees", "eswe"))

## Find First Non-Repeating Character in a String

def findFirstUniqueChar(string):
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

print("Find First Unique Char Implementation")
string = "gdfgfdsf288331167467545-29ikhjfakpas"
print(findFirstUniqueChar(string))

## Find First Non-Repeating Character in a String using List Comprehension
print("List comprehension unique char")
count = [a for a in string if string.count(a) == 1][0]
print(count)

## Find First Non-Repeating Character in a String using Generator
print("generator comprehension unique char")
count = (a for a in string if string.count(a) == 1)
print(next(count))

# Programming Questions Linked Lists

## Check if a linked list contains a cycle, and return the initial node of the cycle if true

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
    def checkIfCycle(self):
        currentNode = self.head
        s = set()
        while currentNode is not None:
            if currentNode in s:
                return (True, currentNode)
            s.add(currentNode)
            currentNode = currentNode.nextNode
        return False

linkedList = LinkedList()
linkedList.insert(10)
linkedList.insert(5)
linkedList.insert(30)
linkedList.insert(3)
linkedList.insert(1)
linkedList.head.nextNode.nextNode.nextNode = linkedList.head.nextNode
print(linkedList.checkIfCycle())

## Finding middle node in single linked list

# Programming Questions Stacks

## Return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory