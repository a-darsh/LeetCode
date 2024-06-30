class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i]+=1
            
        maxHeap = []
        for key,val in hmap.items():
            heapq.heappush(maxHeap, (-val,key))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans