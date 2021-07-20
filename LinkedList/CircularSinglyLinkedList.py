# Title: Circular Linked List
# Author: Ahmed M Khan
# Date Created: 7/19/21
# Date Modified: 7/19/21
# Description : This program creates circular singly linked list; adds and deletes nodes, and traverses circular singly linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    #  Creation of circular singly linked list
    def createCircularSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular SLL has been created"

    #  Insertion of a node in circular singly linked list

    def insertCircularSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"

    # Traversal of a node in circular singly linked list
    def traversalCircularSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching for a node in circular singly linked list
    def searchCircularSLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CircularSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CircularSLL"

    # Delete  a node from circular singly linked list
    def deleteNodeCircularSLL(self, location):
        if self.head is None:
            print("There is not any node in CircularSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire circular sinlgy linked list
    def deleteEntireCircularSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None



circularSLL = CircularSinglyLinkedList()
circularSLL.createCircularSLL(0)
circularSLL.insertCircularSLL(1,1)
circularSLL.insertCircularSLL(2,1)
circularSLL.insertCircularSLL(3,1)

print([node.value for node in circularSLL])
circularSLL.deleteEntireCircularSLL()
print([node.value for node in circularSLL])
