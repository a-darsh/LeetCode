class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0]+=1
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            checkSum = curSum-k
            if checkSum in hmap:
                res+=hmap[checkSum]
            hmap[curSum]+=1
        return res