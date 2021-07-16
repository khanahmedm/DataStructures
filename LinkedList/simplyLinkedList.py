# Title: Singly Linked List
# Author: Ahmed M Khan
# Date Created: 7/15/21
# Date Modified: 7/15/21
# Description : This program creates singly linked list; adds and deletes nodes, and traverses singly linked list

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, val, loc):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
            elif loc == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loc - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverse(self):
        if self.head == None:
            print('This is empty linked list')
        else:
            node = self.head
            while node is not None:
                print(node.val)
                node = node.next

    def search(self, sval):
        if self.head == None:
            print('This is empty linked list')
        else:
            node = self.head
            while node is not None:
                if node.val == sval:
                    return node.val
                node = node.next
            print('The value', sval, 'does not exist in the linked list')

    def delete(self, loc):
        if self.head is None:
            print('This is empty linked list')
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < loc - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


SLL = SLL()
SLL.insert(2,0)
SLL.insert(3,0)
SLL.insert(4,0)
SLL.insert(1,0)
SLL.insert(5,1)
SLL.insert(6,1)
SLL.insert(7,1)
print([node.val for node in SLL])
SLL.insert(9,4)
print([node.val for node in SLL])
#l = list()
#for node in SLL:
#    l.append(node.val)
#print(l)
#SLL.traverse()
#print(SLL.search(4))
SLL.delete(3)
print([node.val for node in SLL])
