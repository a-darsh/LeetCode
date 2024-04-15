class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        def backtrack(perm, index):
            if len(perm)==n:
                if perm not in ans:
                    ans.append(perm)
                return
            for i,num in enumerate(nums):
                if i not in index:
                    backtrack(perm+[num], index+[i])
        
        backtrack([],[])
        
        return ans