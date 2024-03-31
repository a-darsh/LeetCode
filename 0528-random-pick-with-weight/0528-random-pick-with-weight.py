class Solution:

    def __init__(self, w: List[int]):
        
        self.prefixSum = []
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            self.prefixSum.append(cur)
        self.totalSum = cur

    def pickIndex(self) -> int:
        
        n = random.random()*self.totalSum
        l, r = 0, len(self.prefixSum)
        ans = -1
        while(l<r):
            mid = l+ (r-l)//2
            if n>self.prefixSum[mid]:
                l = mid+1
            else:
                r = mid
        
        return l
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()