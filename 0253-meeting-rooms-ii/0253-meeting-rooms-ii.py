import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endtimes = []
        size = 0
        ans = 0
        for meet in intervals:
            while endtimes and endtimes[0]<=meet[0]:
                heappop(endtimes)
                size-=1
            heappush(endtimes, meet[1])
            size+=1
            ans = max(size, ans)
        return ans
            
        
        