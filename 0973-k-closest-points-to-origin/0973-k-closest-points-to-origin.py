class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        hp = []
        
        for i in points:
          dist = (i[0]-0)**2 + (i[1]-0)**2
          hp.append((dist, i[0], i[1]))
        
        heapq.heapify(hp)
        
        res = []
        
        while(k>0):
          
          _, x,y = heapq.heappop(hp)
          res.append((x,y))

          k-=1
          
        return res