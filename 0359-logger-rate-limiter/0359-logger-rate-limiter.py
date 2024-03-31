class Logger:

    def __init__(self):
        self.hmap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hmap:
            if timestamp >= self.hmap[message]:
                self.hmap[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.hmap[message] = timestamp+10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)