class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if self.minList:
            if self.minList[-1]>val:
                self.minList.append(val)
            else:
                self.minList.append(self.minList[-1])
        else:
            self.minList.append(val)
        return

    def pop(self) -> None:
        self.stack.popleft()
        self.minList.pop()
        return

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.minList[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()