class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      
      one, two = cost[-1], 0
      
      for i in range(len(cost)-2, -1, -1):
        temp = cost[i] + min(one, two)
        one, two = temp, one
        
      return min(one, two)
    