#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:07:20 2019

@author: abdur
"""


class linkedList:
    def __init__(self, head):
        self.head = head
        self.size = 1
    
    def printList(self, head):
        itr = head
        while(itr!=None):
            print(itr.data)
            itr = itr.next_node
            
    def deleteNode(self, data):
        itr = self.head
        
        
        if itr.data == data:
            self.head = itr.next_node
        
        while(itr!=None):
            if( itr.next_node!=None  and  itr.next_node.data==data):
                itr.next_node = itr.next_node.next_node
            
            itr = itr.next_node
        
    def reverseList(self):
        current = self.head
        prev =  following = None
        
        while(current!=None):
            following = current.next_node
            current.next_node = prev
            prev = current
            current = following
            
        
        return prev
    
    def insertAtEnd(self,node):
        itr = self.head
        
        
        while(itr.next_node!=None):
            itr = itr.next_node
            
        
        itr.next_node = node
        self.size+=1
        
    def insertAtIndex(self,node,position):
        current = self.head
        
        
        if position<1 or position>self.size+1:
            print("wrong position")
            return
        
        if position == 1:
            node.next_node = current
            self.head = node
        else:
            for i in range(1, position-1):
                current = current.next_node 
            
            node.next_node = current.next_node
            current.next_node = node
            
            
        self.size+=1
        
        
            
    
            
            
class Node:
        
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    
    
    def set_next(self, new_next):
        self.next_node = new_next
        



#%% 

#testing 1

node1 = Node(15)
node2 =  Node(9)
node3 =  Node(19)
node4 =  Node(100)
node5 =  Node(500)
node6 =  Node(300)
node7 =  Node(200)

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node6)
node6.set_next(node7)





linkedList = linkedList(node1)

linkedList.printList(linkedList.head)

#print("After deletion: ")



#linkedList.deleteNode(15)
#linkedList.printList(linkedList.head)


print("After reverse: ")

reverse_head = linkedList.reverseList()
linkedList.printList(reverse_head)        


#%%

#testing 2



list1 = linkedList(Node(11))


list1.insertAtEnd(Node(12))
list1.insertAtEnd(Node(10))
list1.insertAtEnd(Node(15))
list1.insertAtEnd(Node(19))

list1.printList(list1.head)

#reverse_head = list1.reverseList()
#list1.printList(reverse_head)

print("inserting at the beginning")
list1.insertAtIndex(Node(100),1)
list1.printList(list1.head)



print("inserting at the end")
list1.insertAtIndex(Node(200),list1.size+1)
list1.printList(list1.head)


from random import randint

print("inserting at a random position")
list1.insertAtIndex(Node(300), randint(1,list1.size+1))
list1.printList(list1.head)
#%%

#testing 3

