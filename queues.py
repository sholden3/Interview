# Queues are an abstract data type that can be implemented either with arrays, or with linked lists.
# They have a FIFO structure, which means the first item we insert into it is the first item we take out.
# They have the basic operations enqueue(), dequeue() and peek().
# Have several applications within operating systems, as well as thread management (multithreading).
# So if we insert an item 10, then 6, 18, 1, 56, the queue will go left to right.
# So when would we use this? Well, queues are useful when a resource is shared with several consumers (threads).
# threads are stored within queues.
# Queues are important in CPU scheduling.
# When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes.
# Graph algorithms rely heavily on queues: Breadth-first search use queues as an underlying abstract data type.

# Queue is the abstract data type
# If we are just interested in time complexity, not memory complexity, a doubly linked list would be better, as we would have O(1).
# If we are worried about memory complexity, and or the amount of data will be small, we can use the queue.
class Queue:
    def __init__(self):
        # our one dimensional array is our data structure our queue is built on.
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    # O(1) time complexity, because appending a value to the end of an array is always O(1) as we do not have to shift it.
    def enqueue(self, data):
        self.queue.append(data)

    # We want to grab the first element of the array, and remove it. This will be O(N), as though random indexing is always O(1) with arrays,
    # we then need to shift our array, as we now have a hole in it. Remember that because our hole is at the first index, we always have
    # a worse case scenario for shifting our array.
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    
    # O(1) running time.
    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)
        # Could also do it with pointer arithemtic:
        # You would need to import sys to do this
        # import sys
        # return round((id(self.queue[-1]) - id(self.queue[0])) / sys.getsizeof(self.queue[0]))

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Size of queue: %d" % queue.size_queue())
print("Dequeue: %d" % queue.dequeue())
print("Size of queue: %d" % queue.size_queue())