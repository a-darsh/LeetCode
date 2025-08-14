class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        counter = Counter(nums)
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for (count,num) in heap]
        #O(N+mlogk), O(N)