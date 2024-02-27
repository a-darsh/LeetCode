class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        for i in range(1, n//2 + 1):
            if n%i==0:
                ans.append(i)
                
        ans.append(n)
                
        if len(ans) >= k :
            return ans[k-1]
        
        else:
            return -1
        
        