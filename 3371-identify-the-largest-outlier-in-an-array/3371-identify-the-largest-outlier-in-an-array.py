class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        counts = Counter(nums)
        outlier = float('-inf')
        for n in nums:
            counts[n]-=1
            total-=n
            if total%2==0 and counts[total//2]>0:
                outlier = max(outlier, n)
            counts[n]+=1
            total+=n
        return outlier
