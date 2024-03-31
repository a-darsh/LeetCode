class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int) #prefixsum:numbre of ways
        hmap[0] = 1
        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur = cur+nums[i]
            if cur-k in hmap:
                ans+=hmap[cur-k]
            hmap[cur]+=1
        
        return ans
            
            