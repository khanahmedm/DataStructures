class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        
        current = self.head
        node.next = self.head
        self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = node
        
    def get_len(self):
        count = 0
        if not self.head:
            return count
        
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def insert_at_pos(self, data, position):

        if position > self.get_len() + 1:
            return f'position is out of bound. list is too short. please enter {self.get_len() + 1} or less.' 
        elif position == 1:
            self.insert_at_start(data)
            return f'inserted {data} at position {position}.'
        elif position == self.get_len() + 1 :
            self.insert_at_end(data)
            return f'inserted {data} at position {position}.'

        current = self.head
        pos = 1
        node = Node(data)
        while current.next:
            if pos == position:
                node.next = current
                temp.next = node
                return f'inserted {data} at position {position}.'

            temp = current
            current = current.next
            pos += 1
        
    def remove_at_pos(self, position):
        if not self.head:
            return f'the list is empty.'
        elif position > self.get_len():
            return f'cannot remove as list has only {self.get_len()} items.'
        else:
            current = self.head
            pos = 1
            while current:
                if pos == position:
                    if position == 1:
                        self.head = current.next
                        #del current
                    else:
                        temp.next = current.next
                        #del current
                
                temp = current
                current = current.next
                pos += 1
            
            return f'removed item at {position} position.'
    
    def remove_item(self, data):
        if not self.head:
            return 'list is empty.'

        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    if not current.next:
                        temp.next = None
                    else:
                        temp.next = current.next
            
            temp = current
            current = current.next
        
        return f'removed item {data}.'
    
    def display(self):
        if not self.head:
            return 'list is empty'
        else:
            ltr = ''
            current = self.head
            while current:
                ltr += str(current.data) + '-->'
                current = current.next
            return ltr
            

ll = LinkedList()
print(ll.display())
ll.insert_at_start(1)
ll.insert_at_start(2)
ll.insert_at_start(3)
print(ll.display())
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
print(ll.display())
print(ll.get_len())
print(ll.insert_at_pos(7, 7))
print(ll.get_len())
print(ll.display())
print(ll.insert_at_pos(8, 4))
print(ll.get_len())
print(ll.display())
print(ll.remove_at_pos(4))
print(ll.get_len())
print(ll.display())
print(ll.remove_at_pos(1))
print(ll.get_len())
print(ll.display())
print(ll.remove_at_pos(6))
print(ll.get_len())
print(ll.display())
print(ll.remove_item(5))
print(ll.get_len())
print(ll.display())
ll.insert_at_end(2)
print(ll.display())
print(ll.get_len())
print(ll.remove_item(2))
print(ll.get_len())
print(ll.display())
        
        

