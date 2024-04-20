import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k <= 0:
            return []
        
        # Min-heap
        minHeap = []
        # Only push the first element of nums2 with each element of nums1
        for i in range(min(k, len(nums1))):  # Limit to k or total elements in nums1
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while k > 0 and minHeap:
            _, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):  # Push the next element from nums2 with the same nums1[i]
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return ans
