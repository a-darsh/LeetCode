import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        maxRoom = float("-inf")
        curEnds = []
        size = 0
        for meet in intervals:
            while curEnds and curEnds[0] <= meet[0]:
                heapq.heappop(curEnds)
                size-=1
            heapq.heappush(curEnds, meet[1])
            size+=1
            maxRoom = max(maxRoom, size)
        return maxRoom
        
            
        
            
            