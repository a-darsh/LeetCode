from heapq import heappush, heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        used = []  # Will store (end time, room index)
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that are now available
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(available, room)
            
            if available:
                # Use the first available room
                room = heappop(available)
            else:
                # Wait for the next room to be available
                end_time, room = heappop(used)
                # Adjust the meeting start and end times based on the room availability
                end += end_time - start
                start = end_time
            
            # Book the room
            heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count))
