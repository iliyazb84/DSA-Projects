class Stack:
    def __init__(self,Max_Store):
        self._S =[None for i in range(Max_Store)]
        self.pointer= 0
        self.Max= Max_Store
    def push(self,num):
        if self.pointer == self.Max:
            raise Exception ("The Stack is full")
        else:
            self._S[self.pointer] = num
            self.pointer+= 1
            print(f"{num} has benn stored successfully")

    def pop(self):
        if self.IsEmpty():
            raise Exception ("The Stack is Empty")
        else:
            self.pointer -=1
            deleted = self._S[self.pointer]
            print(f"{deleted} has been deleted successfully")
            return deleted
    def peek(self):
        return self._S[self.pointer-1]    
    def IsEmpty(self):
        if self.pointer == 0:
            return True
        return False