

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.head
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def get_all_data(self):
        result = []
        aux = self.head
        while aux:
            result.append(aux.data)
            aux = aux.next
            
        return result