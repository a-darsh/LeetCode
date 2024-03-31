import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        occupied = []
        
        #adding first meeting
        heapq.heappush(occupied, intervals[0][1])
        
        for meeting in intervals[1:]:
            if meeting[0]>=occupied[0]:
                heapq.heappop(occupied)
                heapq.heappush(occupied, meeting[1])
            else:
                heapq.heappush(occupied, meeting[1])
        
        return len(occupied)
                
        
        
        
            
        
            
            