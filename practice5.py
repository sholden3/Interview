## Queue with Stacks (REVIEW)

### Let us start with our two stacks in our Queue.
### We need to have our two stacks as one will contain our enqueue stack, and one our dequeue stack.

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    def enqueue(self, data):
        self.enqueue_stack.append(data)
    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Queue does not have data")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                data = self.enqueue_stack[-1]
                del self.enqueue_stack[-1]
                self.dequeue_stack.append(data)
        data = self.dequeue_stack[-1]
        del self.dequeue_stack[-1]
        return data

queue = Queue()
queue.enqueue(202)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue("ten")
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())

## Queue with Stacks and Recursions (REVIEW)

### Here we want to make use of recursions, instead of a second stack

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

queue = Queue()
queue.enqueue(50)
queue.enqueue(23)
queue.enqueue(2)
queue.enqueue("ten")
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())

## Insertion Sort (REVIEW)

### Here we want to create our O(N^2) insertion sort.
### We will base this off of our firstUnsortedIndex

def insertionSort(arr):
    for firstUnsortedIndex in range(1, len(arr)):
        newElement = arr[firstUnsortedIndex]
        i = firstUnsortedIndex
        while i > 0 and arr[i - 1] > newElement:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = newElement

arr = [1,4,564,233,1,-2,23,0,-11000]
insertionSort(arr)
print(arr)

## Selection Sort (REVIEW)

### This is similar to the insertionSort, but we shift everything at the end, and we start at index 0
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

arr = [23,43434,1,23,3,434,6,8,2,1,23,-123,-32,-23,-32,0,0]
selectionSort(arr)
print(arr)

## Quicksort (REVIEW)

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
        quickSort(arr,low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [23,4,1,0,0,1,-23,-3,-4,-100,-3,1231]
quickSort(arr,0,len(arr)-1)
print(arr)

## Binary Search (REVIEW)

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

print(binarySearch(arr,0, len(arr)-1, 0))

## Special case Duplicate Values in positive int array where largest number is no larger then max size of array (Review)

def dupSpecialIntArray(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = -arr[abs(i)]
        else:
            print(str(abs(i)), "is a dup")

arr = [1,0,3,4,2,3,9,8,7,7,5,6]
dupSpecialIntArray(arr)

## Remove Duplicates from an Array in Place (REVIEW)

### Here we want to actually move all duplicates to the end of the array, and return the index where
### the dups start.

def removeDupsInPlace(arr):
    if len(arr) == 0:
        raise Exception("Array is empty")
    if len(arr) == 1:
        return len(arr)
    i = 0
    for j in range(0, len(arr)-1):
        if arr[j] != arr[j + 1]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i] = arr[-1]
    del arr[-1]
    return i

arr = [23,4,1,0,0,1,-23,-3,-4,-100,-3,1231]
quickSort(arr,0,len(arr)-1)
print("removeDuplicatesInPlace")
print("Partition Index:",removeDupsInPlace(arr))
print(arr)

## Find the missing number in a given integer array of 1 to 100 (REVIEW)

### We want to find the missing number in an array that has continuous numbers starting at 1 all the way
### up to 100.

def getMissingNo(arr):
    total = 1
    for i in range(2, len(arr) + 2):
        total += i
        total -= arr[i - 2]
    return total

arr = [1,2,3,4,5,6,7,8,9,10,12,13,14,15]
print(getMissingNo(arr))

## Find First Non-Repeating Character in a String (REVIEW)

def firstNonRepeatChar(string):
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
    return None

string = "42342jjkjfsidujfsioq100fifiajnj3ahduasodiopac"
print(firstNonRepeatChar(string))

## Find First Non-Repeating Character in a String using List Comprehension (REVIEW)
count = [a for a in string if string.count(a) == 1][0]
print(count)

## Find First Non-Repeating Character in a String using Generator (REVIEW)
count = (a for a in string if string.count(a) == 1)
print(next(count))