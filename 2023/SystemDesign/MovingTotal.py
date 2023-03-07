class MovingTotal:
    def __init__(self):
        self.queue = []
        self.dict = {}
        self.front = 0
        self.initial_sum = 0

    def add(self, nums):
        for i in nums:
            self.queue.append(i)
            if len(self.queue) >= 3 and not self.dict:
                self.initial_sum = sum(self.queue)
                self.dict[self.initial_sum] = 0
                self.front += 1
            elif len(self.queue) >= 3:
                self.initial_sum = self.initial_sum - self.queue[self.front-1] + self.queue[-1]
                self.dict[self.initial_sum] = 0
                self.front += 1
    
    def contains(self, value):
        return value in self.dict
    
    def __str__(self):
        return f"Queue: {self.queue}\nHashMap: {self.dict}"

moving_total = MovingTotal()
moving_total.add([1,2,3,4,5,6,7,8])
print(moving_total)
            