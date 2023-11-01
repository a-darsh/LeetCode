class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        hmap = {}
        def minSearch(i):
            
            if i in hmap:
                return hmap[i]
            
            
            if i>=len(cost):
                return 0
            
            hmap[i] = cost[i] + min(minSearch(i+1), minSearch(i+2))
            return hmap[i]
        
        
        return min(minSearch(0), minSearch(1))
    
        