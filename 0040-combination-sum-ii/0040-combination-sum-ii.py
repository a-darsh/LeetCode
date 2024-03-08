class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        
        def dfs(s, index, cur=[]):
            if s==target:
                ans.append(cur)
                return
            if s>target:
                return
            
            prev = -1
            for i in range(index, len(candidates)):
                if prev==candidates[i]:
                    continue
                prev = candidates[i]
                dfs(s+candidates[i], i+1, cur+[candidates[i]])
            
        dfs(0, 0)
        
        return ans