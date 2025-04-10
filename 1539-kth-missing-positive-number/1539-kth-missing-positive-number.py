class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l,r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            miss = arr[mid]-(mid+1)
            if miss<k:
                l=mid+1
            else:
                r=mid-1
        return k+l

        #O(N), O(1)