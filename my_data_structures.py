class Node:
    """Node class, used to store individual data points in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class LinkedList:

    """Linked list class, which holds the nodes."""
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current:
            if current.next_node is None:
                current.next_node = new_node
                current.next_node.prev_node = current
                return
            else:
                current = current.next_node

    def add_first(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
            
    def display(self):
        current= self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next_node
    
    def search(self, data):
        """Returns a list of indices"""
        target_data = data
        current= self.head
        l = []
        xz = 0
        while current:
            if current.data is target_data:
                l.append(xz)
            xz = xz+ 1 
            current = current.next_node
        return l
    
    def find_difference(self, data, targt):
        target_data = data

    
    def subtract(self, data):
        current = self.head
        target = data

        while current:
            if current.next_node.data == target:
                current.next_node = current.next_node.next_node
                current = current.next_node
                return
            current = current.next_node
            


    def count_occurences(self, data):
        return len(self.search(data))

    def print_prev(self, data):
        target_data = data
        current= self.head
        while current:
            if current.data is target_data:
                print("this is previous node:", current.prev_node.data)
            current = current.next_node
        return 


    def print_head(self):
        print("This is head =", self.head.data)

    def find_final(self):
        current=  self.head
        index = 0 
        while current:
            if current.next_node is None:
                self.tail = current
                
                return f"This is tail: {current.data} at index: {index}"
            index = index +1 
            current = current.next_node

# Stack is LIFO, Queue is FIFO

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        current = self.head

        if current == None:
            self.head = new_node
            return

        while current:
            if current.next_node is None:
                current.next_node = new_node
                self.tail = current.next_node
                return
            current = current.next_node
    
    def remove(self):
        """Removes the last item"""
        current = self.head
        while current: 
            if current.next_node == self.tail:
                current.next_node = current.next_node.next_node
                self.tail = current
                current = current.next_node
                return 
            current = current.next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end= " - ")
            current = current.next_node
        print("None")

## Date: September 16-17, 2023
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, data):
        new_node = Node(data)
        current = self.head

        if current == None:
            self.head = new_node
            return

        while current:
            if current.next_node is None:
                current.next_node = new_node
                self.tail = current.next_node
                return
            current = current.next_node
    
    def remove(self):
        """Removes the first item"""
        current = self.head

        current = current.next_node
        self.head = current
        
        return 
        current = current.next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end= " - ")
            current = current.next_node
        print("None")

