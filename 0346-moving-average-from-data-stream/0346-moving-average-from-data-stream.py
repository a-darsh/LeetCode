class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.queue = []
        self.sum = 0

    def next(self, val: int) -> float:
        if self.count<self.size:
            self.queue.append(val)
            self.sum+=val
            self.count+=1
            return self.sum/self.count
        else:
            remEle = self.queue.pop(0)
            self.queue.append(val)
            self.sum = self.sum -remEle+val
            return self.sum/self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)