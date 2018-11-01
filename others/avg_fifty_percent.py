class AvgFiftyPercent:
    def __init__(self, max_num):
        self.max_num = max_num
        self.array = [0] * max_num
        self.count = 0

    def add(self, num):
        if num <= self.max_num:
            self.array[num - 1] += 1
            self.count += 1

    def get(self):
        current = 0
        sum = 0
        num_items = 0
        for i, item in enumerate(self.array):
            if item:
                counter = 0
                while counter < item:
                    current += 1
                    counter += 1
                    if (self.count / 4 < current) and (current < 3 * self.count / 4):
                        sum += i + 1
                        num_items += 1

        return sum / num_items


avg = AvgFiftyPercent(10)
avg.add(1)
avg.add(2)
avg.add(3)
avg.add(3)
avg.add(3)
#avg.add(5)
avg.add(3)
avg.add(5)
avg.add(3)
#avg.add(6)
print(avg.get())
