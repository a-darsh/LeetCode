class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque([])
        self.total = 0
    def next(self, val: int) -> float:
        if len(self.window)==self.size:
            temp = self.window.popleft()
            self.total-=temp
        self.window.append(val)
        self.total+=val
        return self.total/len(self.window)
        #O(1), O(N)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)