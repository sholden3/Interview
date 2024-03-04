# We want to design an algorithm that can return the maximum item of a stack within O(1) running time complexity, and we can use O(N) extra memory.
# We can make use of another stack to track the max item.

# The problem is that we have a stack, and we want to track the largest item during insertion.
# We want to make sure that our getMax() operation has O(1) running time.
# The memory complextion can be O(N), which means that we can use another stack in the implementation.
# So we will have two stacks then, the main stack, and the max stack.
# So what we want to do is when we get our first item, we want to insert it into the main stack, and the max stack.
# When we get our second item, we want to insert it into the main stack, and check the max stack to see if the last item on
# the maximum stack is greater than the last item. If it isn't we want to duplicate the maximum item in the max stack, if it is
# greater, than we want to add it. We keep on doing this.
# We will then just use the pop method to get the max item from the maxStack. This gives us our O(N) memory needed (as we are duplicating the stack size),
# but we get our O(1) running time. We can change this up, where we do not duplicate the last item if need be.

class Stack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)
        if self.stack_size() == 1:
            self.max_stack.append(data)
        elif self.max_stack[-1] <= data:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.stack_size() > 0:
            del self.max_stack[-1]
            data = self.main_stack[-1]
            del self.main_stack[-1]
            return data
        else:
            return -1

    def peek(self):
        return self.main_stack[-1]

    def stack_size(self):
        return len(self.main_stack)

    def get_max_item(self):
        data = self.max_stack[-1]
        del self.max_stack[-1]
        return data

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(40)
stack.push(-1)
stack.push(10)

print(stack.main_stack)
print(stack.max_stack)
print(stack.pop())
print(stack.main_stack)
print(stack.max_stack)
print(stack.get_max_item())
print(stack.main_stack)
print(stack.max_stack)

# Queue Implementation with Stacks

# The problem is that we want to implement a queue abstract data type with the enqueue() and dequeue() operations with stacks.
# We can use two stacks to solve this problem.
# One stack for the enqueue() operations, and one stack for the dequeue() operations.

# So for every item that we want to go ahead and enqueue, we need to add to the enqueue stack. When we want to dequeue our queue, we should return the first item
# we have inserted, because queues have a FIFO structure. But because we are using a stack, we cannot access the first item.
# So if our dequeue stack is empty, we want to pop off the items from our enqueue stack one by one into the dequeue stack. This essentially reverses the stack.
# Now we can call the dequeue queue pop method to get the items from the dequeue stack. And we keep on doing this.
# While our dequeue stack is not empty, we keep popping items off of it. Even if we add items to our enqueue stack. If we go to dequeue our queue, and there
# are no items on the dequeue stack, we pop off each item from the enqueue stack to the dequeue stack.

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

# We wamt to do the same as before, but with a single stack and recursive calls.
# What we want to do is pop off all of the items until we get to the last item. We then want to return that item, and recreate the stack itself.

class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    # We use 2 stacks again, but instead of us explicitly defining the second stack we usee the call-stack of program (the stack memory, or execution stack)
    def dequeue(self):
        # base case for the recursive method calls the first item
        # is what we are after (this is what we need for queue's dequeue operation)
        if len(self.stack) == 1:
            return self.stack.pop()

        # we keep popping the item until we find the last one
        item = self.stack.pop()

        # we call the method recursively until we find the first item we have inserted
        dequeued_item = self.dequeue()

        # After we find the item we have to reinsert the items one by one
        self.stack.append(item)

        # this is the item we are looking for (this is what has been popped off in the stack.size()==1 section)
        return dequeued_item

queue = Queue()
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(50)
queue.enqueue(3)
print(queue.stack)
print(queue.dequeue())
print(queue.stack)

