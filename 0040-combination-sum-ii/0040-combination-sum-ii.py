class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans  = []
        candidates = sorted(candidates)
        def dfs(total, index, cur):
            
            if total==target:
                self.ans.append(cur)
            
            if total>target:
                return
            prev = -1
            for i in range(index, len(candidates)):
                if prev==candidates[i]:
                    continue
                dfs(total+candidates[i], i+1, cur+[candidates[i]])
                prev = candidates[i]
            
                
        dfs(0,0,[])
        return self.ans
        