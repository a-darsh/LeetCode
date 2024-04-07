class HitCounter:

    def __init__(self):
        self.timeList = []
        self.counter = 0

    def hit(self, timestamp: int) -> None:
        self.timeList.append(timestamp)
        self.counter+=1

    def getHits(self, timestamp: int) -> int:
        while self.timeList and self.timeList[0]+300<=timestamp:
            self.timeList.pop(0)
            self.counter-=1
        return self.counter
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)