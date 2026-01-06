
class Queue:
    def __init__(self):
        self.inStack = [] #? Each Elements Goes in This First (Front --> Rear)
        self.outStack = [] #? For Dequeueing, Front Element Goes into This (Front <-- Rear)

    #! Adding To Queue
    def enqueue(self, data):
        self.inStack.append(data)
        
    #! Removes From Queue
    def dequeue(self):

        #? Checks if OutStack is Empty (Front Element Goes into This)
        if not self.outStack:
            if not self.inStack: #? Maybe There Is Nothing in Queue At All?
                raise IndexError("Nothing in Queue...")

            #? Pouring All Elements from inStack --> outStack
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        
        return self.outStack.pop()

    #! Returns the Front Element    
    def peek(self):
        if not self.outStack:
            if not self.inStack:
                raise IndexError("Nothing in Queue...")

            while self.inStack:
                self.outStack.append(self.inStack.pop())

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

