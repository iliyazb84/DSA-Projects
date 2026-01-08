class Node:
    def __init__(self,data=-1):
        self.data=data
        self.Next=None

class link_list:
    def __init__(self):
        self.head = None
    
    def InsertAtIndex(self,data, index):
        new_node = Node(data)
        if index == 0:
            new_node.Next = self.head
            self.head = new_node
            return
        
        Previous_Node = self.Find_Index(index-1)
        if Previous_Node == None:
            print("Index out of range!")
            return
        new_node.Next=Previous_Node.Next
        Previous_Node.Next=new_node

        
    def Find_Index(self,Index):
        current=self.head
        for i in range (0,Index):
            if current == None:
                return None 
            current = current.Next
        return current
    
    def InsertAtEnd(self, data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            return
        current=self.head
        while current.Next != None:
            current=current.Next
        current.Next=new_node
    


    