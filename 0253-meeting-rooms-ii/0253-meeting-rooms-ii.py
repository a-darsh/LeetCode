import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        occupied = []
        count=0
        for interval in intervals:
            if occupied and occupied[0]<=interval[0]:
                heapq.heappop(occupied)
                heapq.heappush(occupied, interval[1])
            else:
                heapq.heappush(occupied, interval[1])
                count+=1
        return count
        
        
        
            
        
            
            