'''
creating linked list class
'''
class LL:

    def __init__(self):
        self.head=None

    #add node at the starting
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    #add after a node
    def insert(self,prev_node,new_data):
        new_node=Node(new_data)
        if prev_node is None:
            print("node does'nt exist")
        else:
            new_node.next=prev_node.next
            prev_node.next=new_node

    #add at the end
    '''
        first check that the ll is_empty or not
        then traverse to the last node
        then add the node at the end
    '''
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while(last.next):
                last=last.next
            last.next=new_node
        return "done"

    #print all nodes
    def display(self):
        if self.head is not None:
            temp=self.head
            while(temp):
                print(temp.data,end=" --> ")
                temp=temp.next
            print("\n")
        else:
            print("list is empty")
        
    #delete a node by value
    def delete(self,key):
        temp=self.head
        '''chech if ll  is_empty or not
           then check that the key is head value or not
           if key is head the delete the head
        '''
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None

            #if key is not head value then traverse to that node and delete that node

            while(temp):
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev.next=temp.next
            temp=None
        else:
            print("linked list is empty")

    #delete a node by position
    def delete_pos(self,pos):
        temp=self.head
        if self.head is not None:
            if pos==0:
                self.head=temp.next
                temp=None
            else:
                for i in range(pos-1):
                    prev=temp
                    temp=temp.next
                prev.next=temp.next
                temp=None
        else:
            print("linked list is empty")

    #delete the linked_list
    def delete_list(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            temp=self.head
            while(temp):
                prev=temp.next
                del temp.data
                temp=prev
            print("list cleared")
            self.head=None
            return

    #lenght of the ll
    def length(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return (count)

    #search in the ll
    def search(self,key):
        if self.head is not None:
            temp=self.head
            count=0
            while(temp):
                count+=1
                if temp.data==key:
                    return print(True,"at position",count)
                temp=temp.next
            return print(False)


    #get N th nodein the ll
    def get_node(self,pos):
        temp=self.head
        for i in range(1,pos):
            temp=temp.next
        print(temp.data)

    #get N th node from the end
    def get_node_end(self,pos):
        l=self.length()
        temp=self.head
        for i in range(l-pos):
            temp=temp.next
        print(temp.data)
        

'''creating node class
'''
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

l = LL() 
l.append('London') 
l.append('Kolkata') 
l.append('Delhi') 
l.append('Patna') 
l.append('Mumbai')
l.display()
