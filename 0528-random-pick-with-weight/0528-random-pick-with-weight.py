class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        self.total = 0
        for i in w:
            self.total+=i
            self.prefixSum.append(self.total)

    def pickIndex(self) -> int:
        pick = random.random()*self.total
        l,r = 0, len(self.prefixSum)
        while l<r:
            mid = (l+r)//2
            if self.prefixSum[mid]>=pick:
                r = mid
            else:
                l = mid+1
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()