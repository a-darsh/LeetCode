class MinStack:

    def __init__(self):
        self.lst = []
        self.size = 0

    def push(self, val: int) -> None:
        self.lst.append(val)
        self.size = self.size + 1

    def pop(self) -> None:
        self.lst = self.lst[:-1]
        self.size = self.size - 1

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
      return min(self.lst)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()