'''
implementing stack using linked list
'''


class StackNode:

    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:

    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=StackNode(data)
        if self.top is None:
            self.top=new_node
            return
        else:
            new_node.next=self.top
            self.top=new_node
            return

    def pop(self):
        if self.top is None:
            print("stack is emptyu")
            return
        else:
            temp=self.top
            self.top=self.top.next
            print(temp.data)
            return

    def peek(self):
        if self.top is None:
            print("stack is emptyu")
            return
        else:
            print(self.top.data)
            return

        
            
        
