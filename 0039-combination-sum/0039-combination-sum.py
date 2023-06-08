class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        cur = []
        #i ->from which index to include
        #ans -> ans list
        #cur -> current list
        #total -> current total
        def dfs(i, cur, total):
          
          if total == target:
            ans.append(cur.copy())
            return
          
          if i >= len(candidates) or total > target:
            return
          
          #first recursion including the candidate i
          cur.append(candidates[i])
          dfs(i, cur, total + candidates[i])
          
          #second recursion not including the candidate i
          cur.pop()
          dfs(i+1, cur, total)
          
        
        dfs(0, cur, 0)
        
        return ans
        
        
        
        