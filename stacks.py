# Stacks are an abstract data type, which we can implement with either an array, or with a linked list.
# It has a LIFO structure, which means that the last item we inserted will be the first item we take out.
# Our basic operations with it are pop(), push(), and peek().
# Most modern programming languages are stack-oriented.
# They define most basic operations (adding two numbers) as taking their arguments from the stack, and placing any return values back on the stack.

# So let us look at some of the applications of stacks that we can use:

# We use this within stack-oriented programming languages.
# Graph algorithms rely heavily on stacks such as depth-first search can be implemented with stacks.
# Finding Eulerian cycles in a G(V,E) graph.
# Finding strongly connected components in a given G(V,E) graph.

# Stack in memory management.
# There are 2 main types of memory: stack memory and heap memory.
# The stack memory is a special region in the RAM. This is a special data type (stack) that store the active functions and local variables as well.
# This is how Python knows where to return after finish execution of a given function.
# We also have our heap memory, which is a special region in the RAM as well. The size of the heap memory is way larger than that of the stack memory. But the stack memory is faster.
# We store our objects on the heap memory.
# So let us break this down:
# Stack Memory
# small size
# fast access
# stores function calls and local variables
# no fragmentation
# Heap Memory
# large size
# slow access
# stored objects
# may become fragmented
# This means that as python removes certain given objects from the heap, there will be empty and unused regions in the heap memory itself.

# Now the stack data type is implemented with an abstract data type. It also implements the LIFO, which means the last element in
# is the first element out.

# Now the heap memory that we are talking about here has nothing to do with the heap data structure. They just share the name heap.

# So let us break down the stack. This will also help you understand recursion better. When we define a function like so:

def func1():
    return

# Within a our stack we will create a frame from our func1() method. Remember that when we create a function in python, python
# tracks it and stores it on the stack memory. Now let us say that we have a local variable in our function:

def func1():
    variable1 = 1
    return

# This variable in the functions local scope will be stored within the functions frame in the stack method. But what if we call
# a function within a function:

def func1():
    variable1 = 1
    func2(2)
    return

def func2(i):
    variable2 = 2.00
    return

# Our func2 does not get added to the func1 frame. It gets its own frame ontop of the func1 frame. So you can view it as stacking
# on top of each other. That also means that when we evaluate the functions in our stack, we will evaluate the func2 call first,
# and then propagate up to the func1 function with the value evaluated from the func2 call. As well as this, the parameter i
# passed into func2, as well as variable2 will be stored within our func2 stack.

# What about if we called a third function?

def func1():
    variable1 = 1
    func2(2)
    return

def func2(i):
    variable2 = 2.00
    func3()
    return

def func3():
    return

# As you can probably already guess at this point, function three will be pushed onto the stack memory within its own frame. This
# func3 call is now the top frame of our stack.
# So we can see how function calls, local variables, and parameters are stored on the stack memory itself.

# But what if we had a class instead of a function:

class Npc:
    health = 10
    strength = 5
    name = "Gregg"

# So let us reference our class, or object, into our func3 method:

def func3():
    gregg_ref = Npc()

# Remember that we do not actually store our object into our local scope here, but simply a reference, or pointer, to our object
# in memory. This means that although we store our func3 within its own frame in the stack, our object, as well as all of its class
# related variables, will be stored within the heap. And remember, it doesn't matter if we are defining class variables, or instance variables
# in our class, if they are associated with the class, they are stored within the class in the heap. But the reference to this
# object in the heap will be stored within the func3 frame in the stack itself.

# So now we have our stack that contains the func3 frame at the top, then the func2 frame, and then the func1 frame. Remember
# that the stack is a filo (first in last out) data structure. When func3 is completed, it will then move on to func2, and then func1.
# It will also remove the function calls from the stack as it goes through. When func3 is removed, we are also removing the reference to our object, but
# not the object itself. What happens instead is that our object is flagged to be eligible for garbage collection. It has no references to it,
# so it is not being used. For languages like C that do not have a garbage collector, that is why when you create an object that lives in the
# heap through something like malloc, you need to collect it once you are done using it.

# So let us look at implementing a stack data type.
# Remember that stacks have a LIFO structure, which means last in first out.

class Stack:

    def __init__(self):
        # The stack itself is going to be a one dimensional array.
        # Remember that a stack is simply an abstract data type built upon the array.
        # It isn't a data structure itself.
        self.stack = []

    # insert item into the stack
    def push(self, data):
        # We want to always append the data to the end of the stack.
        # Because we are appending data to the end of the array, we have ordo 1 constant running time.
        self.stack.append(data)

    # remove and return the last item in the stack.
    def pop(self):
        # we could just pop the data out, but we want to also look at how to do it manually
        # return self.stack.pop()
        # we store the last value that we want into our data variable.
        data = self.stack[-1]
        # We then delete the last value from the stack itself.
        del self.stack[-1]
        # remember that because we are not creating any holes within out data, and we benefit from random indexing, this is in
        # ordo 1 constant time.
        return data

    # peek: returns the last item without removing it O(1)
    def peek(self):
        return self.stack[-1]

    # Check if it is empty or not in O(1) running time.
    def is_empty(self):
        return self.stack == []

    # Get the size of the stack.
    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.pop())
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.peek())
print('size: %d' % stack.stack_size())

# Now if we were to call pop a bunch of times, we are going to run into an error. So we need to go back and change the implementation of our stack:

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        # We could also use is_empty
        if self.stack_size() < 1:
            return -1
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data
        
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.pop())
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.peek())
print('size: %d' % stack.stack_size())
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.pop())
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.pop())
print('size: %d' % stack.stack_size())
print('last item: %d' % stack.pop())

# So let us look at the real world applications of the stack. Stacks are used for the back button in a web browser, the recently
# visited websites and urls are pushed onto the stack, and the back button pops these urls.
# The undo operation in software does the exact same thing.
# Stack memory implements the stack abstract data type and is used to store local variables and function calls.