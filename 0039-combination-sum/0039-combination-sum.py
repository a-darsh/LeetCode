class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans  = []
        
        def dfs(total, index, cur):
            if total==target:
                self.ans.append(cur)
                
            if total>target:
                return
            
            for i in range(index, len(candidates)):
                dfs(total+candidates[i], i, cur+[candidates[i]])
                
        dfs(0,0,[])
        
        return self.ans
        
        
            