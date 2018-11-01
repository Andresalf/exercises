class None:
    def __init__(self, data):
        self.data = data;
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elems = None

    def push(self, data):
        if not self.head and not self.tail:
            self.head = self.tail = Node(data)
