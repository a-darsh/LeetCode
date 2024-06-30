class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -n)
        
        for i in range(k):
            temp = heapq.heappop(maxHeap)
        
        return -temp