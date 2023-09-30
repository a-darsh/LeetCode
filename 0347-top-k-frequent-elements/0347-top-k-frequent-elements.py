class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
      hmap = {}
      for i in nums:
        if i in hmap:
          hmap[i] += 1
        else:
          hmap[i] = 1
          
      heap = []
      
      for key,val in hmap.items():
        heappush(heap, (-val,key))
        
      ans = []
      while(k>0):
        ans.append(heappop(heap)[1])
        k -= 1
        
      return ans
        