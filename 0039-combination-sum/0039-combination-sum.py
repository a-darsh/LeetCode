class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
    
        def dfs(s, index, cur=[]):
            if s==target:
                ans.append(cur)
                return
            if s>target:
                return
            for i in range(index,len(candidates)):
                dfs(s+candidates[i], i, cur+[candidates[i]])
        
        dfs(0,0)
        
        return ans
        
        
            