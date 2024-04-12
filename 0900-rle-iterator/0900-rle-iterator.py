class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding  = encoding

    def next(self, n: int) -> int:
        while n and self.encoding:
            count, num = self.encoding[0], self.encoding[1]
            if n>count:
                n = n-count
                self.encoding.pop(0)
                self.encoding.pop(0)
            elif n==count:
                n = n-count
                self.encoding.pop(0)
                res = self.encoding.pop(0)
            else:
                self.encoding[0] = count-n
                res = self.encoding[1]
                n=0
        
        if not self.encoding and n>0:
            return -1
        return res
                
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)