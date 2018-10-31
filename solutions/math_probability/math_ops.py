class Solution(object):

    def __init__(self, upper_limit=100):
        self.upper_limit = upper_limit
        self.array = [0] * (self.upper_limit + 1)
        self.max = 0
        self.min = upper_limit
        self.mean = 0
        self.mode = 0
        self.sum = 0
        self.count = 0
        self.max_occurrences = 0

    def insert(self, val):
        if val is None:
            raise TypeError
        if val >= 0 and val <= self.upper_limit:
            self.count += 1
            self.array[val] += 1
            if val > self.max:
                self.max = val
            if val < self.min:
                self.min = val
            self.sum += val
            self.mean = self.sum / self.count
            if self.array[val] > self.max_occurrences:
                self.max_occurrences = self.array[val]
                self.mode = val
            