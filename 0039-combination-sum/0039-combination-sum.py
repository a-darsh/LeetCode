class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def backtrack(start, comb, curTarget):
            if curTarget==0:
                ans.append(comb)
                return 
            if curTarget<0:
                return
            for i,num in enumerate(candidates[start:]):
                backtrack(start+i, comb+[num], curTarget-num)
        
        backtrack(0, [],target)
        return ans