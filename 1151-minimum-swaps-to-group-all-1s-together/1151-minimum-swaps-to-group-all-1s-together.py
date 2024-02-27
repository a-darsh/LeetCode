class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        #slicing window algo
        
        L, N = len(data), sum(data)
        
        cur = minSwap = data[:N].count(0)
        
        for i in range(N, L):
            
            cur += data[i-N]
            cur -= data[i]
            
            minSwap = min(minSwap, cur)
            
        return minSwap
        
        
        