from data_types.priority_queue_node import PriorityQueueNode

'''
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

0 -> 1, 2
1 -> 3, 4
2 -> 5, 6
3 -> 7, 8
4 -> 9, 10

parent = (child - 1) // 2
'''
class MaxPriorityQueue(object):
    def __init__(self):
        self.array = []
    
    def insert(self, node):
        self.array.append(node)
        self.percolate_up(len(self.array) - 1)
        
    def percolate_up(self, child):
        parent = (child - 1) // 2
        while parent >= 0:
            if self.array[child].key > self.array[parent].key:
                self.array[child], self.array[parent] = self.array[parent], self.array[child]
            child = parent
            parent = (child - 1) // 2

    def max(self):
        if not self.array:
            return None
        return self.array[0].obj
        
    def extract_max(self):
        min_node = None
        if self.array:
            min_node = self.array[0]
            last_node = self.array.pop()
            if self.array:
                self.array[0] = last_node
                self.percolate_down(0)
                
        return min_node
        
    def percolate_down(self, parent):
        child = parent * 2 + 1
        while child <= len(self.array) - 1:
            if child + 1 < len(self.array):
                child = child if self.array[child].key > self.array[child + 1].key else child + 1
            if self.array[parent].key < self.array[child].key:
                self.array[parent], self.array[child] = self.array[child], self.array[parent]
            parent = child
            child = parent * 2 + 1
             
    def increase_key(self, obj, new_key):
        for i, node in enumerate(self.array):
            if node.obj == obj:
                if node.key < new_key:
                    node.key = new_key
                    self.percolate_up(i)
                break
                
        