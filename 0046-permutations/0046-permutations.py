class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans=[]
        
        def backtrack(perm):
            if len(perm)==n:
                ans.append(perm)
                return 
            
            for num in nums:
                if num not in perm:
                    backtrack(perm+[num])
        
        backtrack([])
        return ans