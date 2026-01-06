
class Queue:
    def __init__(self):
        self.inStack = [] #? Each Elements Goes in This First (Front --> Rear)
        self.outStack = [] #? For Dequeueing, Front Element Goes into This (Front <-- Rear)

    #! Transfers inStack Element onto outStack
    def transfer(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

    #! Checks if Queue is Empty
    def is_empty(self):
        return not self.outStack and not self.inStack

    #! Adding To Queue
    def enqueue(self, data):
        self.inStack.append(data)
        
    #! Removes From Queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Nothing in Queue...")

        #? Checks if OutStack is Empty (Front Element Goes into This)
        if not self.outStack:

            #? Pouring All Elements from inStack --> outStack
            self.transfer()

        return self.outStack.pop()

    #! Returns the Front Element    
    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing in Queue...")

        if not self.outStack:
            self.transfer()

        #? "-1" Returns Last Index (The Front Element)
        return self.outStack[-1]
    

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.peek())   # Output: 10

# Dequeue elements
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20

# Enqueue another element
queue.enqueue(40)

print(queue.dequeue())  # Output: 30
print(queue.dequeue())  # Output: 40

