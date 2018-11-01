import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def push(self, data):
        heapq.heappush(self.heap, -data)

    def pop(self):
        if len(self.heap):
            return -heapq.heappop(self.heap)

        return IndexError

    def max(self):
        if len(self.heap):
            return -self.heap[0]

        return IndexError

    def __repr__(self):
        return " ".join(str(-c) for c in self.heap)


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def push(self, data):
        heapq.heappush(self.heap, data)

    def pop(self):
        if len(self.heap):
            return heapq.heappop(self.heap)

        return IndexError

    def min(self):
        if len(self.heap):
            return self.heap[0]

        return IndexError

    def __repr__(self):
        return " ".join(str(c) for c in self.heap)


class Median:
    def __init__(self):
        self.min_h = MinHeap()
        self.max_h = MaxHeap()

    def add(self, number):
        if self.min_h.size() == 0 and self.max_h.size() == 0:
            self.max_h.push(number)
        else:
            if number < self.max_h.max():
                if self.max_h.size() > self.min_h.size():
                    self.min_h.push(self.max_h.pop())

                self.max_h.push(number)
            else:
                if self.max_h.size() == self.min_h.size():
                    self.max_h.push(self.min_h.pop())

                self.min_h.push(number)

    def get(self):
        if (self.min_h.size() + self.max_h.size()) % 2 == 0:
            return (self.min_h.min() + self.max_h.max()) / 2

        return self.max_h.max()

    def __repr__(self):
        return str(self.max_h) + " " + str(self.min_h)


m = Median()
m.add(2)
print("list: " + str(m))
print("median: " + str(m.get()))
print

m.add(5)
print("list: " + str(m))
print("median: " + str(m.get()))
print

m.add(6)
print("list: " + str(m))
print("median: " + str(m.get()))
print

m.add(4)
print("list: " + str(m))
print("median: " + str(m.get()))
print

m.add(9)
print("list: " + str(m))
print("median: " + str(m.get()))
print
