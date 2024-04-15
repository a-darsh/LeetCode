class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        n=len(candidates)
        def backtrack(start, comb, cur):
            if cur==0:
                ans.append(comb)
                return
            if cur<0:
                return
            for i in range(start, n):
                backtrack(i, comb+[candidates[i]], cur-candidates[i])
                
        
        backtrack(0,[], target)
        return ans