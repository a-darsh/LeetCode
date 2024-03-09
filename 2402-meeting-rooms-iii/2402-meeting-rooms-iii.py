class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        used = []
        available = [i for i in range(n)]
        count = [0]*n
        
        meetings.sort()
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(available, room)
            
            if available:
                room = heappop(available)
                heappush(used, (end, room))
                count[room] += 1
            else:
                nextEnd, room = heappop(used)
                end = end + nextEnd-start
                heappush(used, (end, room))
                count[room] += 1
        
        return count.index(max(count))
        
        
        