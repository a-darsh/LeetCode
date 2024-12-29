class MinStack:

    def __init__(self):
        self.stck = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.minList:
            self.minList.append(val)
        else:
            self.minList.append(min(self.minList[-1], val))

    def pop(self) -> None:
        self.stck.pop()
        self.minList.pop()
    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        if not self.minList:
            return []
        return self.minList[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()