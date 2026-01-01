class Queue:
    def __init__(self,n):
        self._Q=[ None for _ in range(n)]
        self.Max = n - 1
        self._front=0
        self._rear=0
        
    def add(self,num):
        if self.IsFull() :
            raise Exception ("The Saf is Full!")

        else:
            self._Q[self._rear] = num
            self._rear += 1
            print(f"{num} is successfully added to the saf")

    def deleteq(self):
        if self.IsEmpty():
            raise Exception ("The Saf is Empty!")
        else:
            deleted =self._Q[self._front]
            self._front += 1
            print(f"{deleted} has been deleted successfully")

    def IsEmpty(self):
        if self._front == self._rear:
            return True
        return False
    def IsFull(self):
        if self._rear > self.Max:
            return True
        return False