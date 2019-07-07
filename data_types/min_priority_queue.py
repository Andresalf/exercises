from data_types.priority_queue_node import PriorityQueueNode

'''
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

1 -> 2, 3
2 -> 4, 5
3 -> 6, 7
4 -> 8, 9
5 -> 10, 11

'''
class MinPriorityQueue(object):

    def __init__(self):
        self.array = []
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, node):
        if not self.size:
            self.array = [None]
        self.array.append(node)
        self.size += 1
        self.percolate_up(self.size)

    def min(self):
        if not self.array:
            return None
        return self.array[0].obj
        
    def percolate_up(self, child):
        parent = child // 2
        while parent > 0:
            if self.array[child].key < self.array[parent].key:
                self.array[child], self.array[parent] = self.array[parent], self.array[child]
            child = parent# // 2
            parent = child // 2
    
    def extract_min(self):
        min_node = None
        if self.size:
            min_node = self.array[1]
            last_node = self.array.pop()
            self.size -= 1
            if self.size:
                self.array[1] = last_node
            else:
                self.array = []
            self.percolate_down(1)
            
        return min_node

    def percolate_down(self, parent):
        child = parent * 2
        while child <= self.size:
            if child + 1 <= self.size:
                child = child + 1 if self.array[child].key > self.array[child + 1].key else child
            if self.array[parent].key > self.array[child].key:
                self.array[parent], self.array[child] = self.array[child], self.array[parent]
            parent = child
            child = parent * 2
    
    def decrease_key(self, obj, new_key):
        for i, node in enumerate(self.array):
            if node and node.obj == obj:
                if new_key < node.key:
                    node.key = new_key
                    self.percolate_up(i)
                break
                