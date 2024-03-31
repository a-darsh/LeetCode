from heapq import heappop, heappush
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        occup = [] #(endtime, num)
        count = [0]*n
        
        for start, end in meetings:
            
            while occup and occup[0][0]<=start:
                _,room = heappop(occup)
                heappush(free, room)
            
            if free:
                room = heappop(free)
                heappush(occup,(end, room))
                count[room]+=1
            else:
                earlyEnd, room = heappop(occup)
                newEnd = end + earlyEnd-start
                heappush(occup, (newEnd, room))
                count[room]+=1
        
        maxVal = max(count)
        print(count)
        return count.index(maxVal)
        