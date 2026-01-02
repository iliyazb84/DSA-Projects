
# Creating Queue Using Circular Method.

class Queue:
    def __init__(self, size):        
        # Defining Queue.
        self.queue_size = size
        self.Queue = [None] * self.queue_size

        # Defining Pointers to See Front and Rear Elements!
        self.front = self.rear = -1

    #! Checks if Queue is Full
    def is_full(self):
        return (self.rear + 1) % self.queue_size == self.front
    
    #! Checks if Queue is Empty
    def is_empty(self):
        return self.front == -1
    
    #! Adding Data To Queue
    def enqueue(self, data):
        if self.is_full():
            print("The Queue is Full and Cannot Add Anymore Data!")
            return

        # First Element to Add inside Queue
        if self.is_empty():
            self.front = self.rear = 0
            self.Queue[self.rear] = data
            return
        
        self.rear = (self.rear + 1) % self.queue_size
        self.Queue[self.rear] = data

    #! Removing Front Element from Queue
    def dequeue(self):
        if self.is_empty():
            print("The Queue is Empty and There is Nothing to Remove!")
            return
        
        self.Queue[self.front] = None

        # No More Elements Inside Queue, so Turn it Into an Empty one!
        if self.front == self.rear:
            self.front = self.rear = -1
            return

        self.front = (self.front + 1) % self.queue_size

    #! Seeing What Front Element is
    def peek(self):
        print (f"The Front Element is: {self.Queue[self.front]}")

    #! Reversing Queue's Order
    def reverse_queue(self):
        tempQueue = [None]
        for i in range(self.queue_size - 1, -1, -1):
            tempQueue.append(self.Queue[i])
        self.Queue = tempQueue
        print(f"Here is Your Queue Reversed:\n{self.Queue}")

    #! Printing Normal Queue
    def print_queue(self):
        print(f"Your queue:\n{self.Queue}")

myqueue = Queue(5)
myqueue.print_queue()
myqueue.enqueue(3)
myqueue.enqueue(5)
myqueue.enqueue(2)
myqueue.print_queue()
myqueue.peek()
myqueue.dequeue()
myqueue.peek()
myqueue.print_queue()
myqueue.reverse_queue()
myqueue.reverse_queue()


# while(True):
#     print ("[0] Add Data to Queue\n[1] ")
#     key = int(input("\nEnter your action: "))