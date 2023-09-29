class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key = lambda x:x[1])
        
        heap = []
        maxtime = 0
        
        for time, endtime in courses:
          heappush(heap, -time)
          maxtime += time
          
          if maxtime > endtime:
            bigtime = heappop(heap)
            maxtime += bigtime
        
        print(heap)
            
        return len(heap)
          