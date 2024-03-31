from heapq import heappop, heappush
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Ensure meetings are sorted by start time
        free = [i for i in range(n)]
        occup = []  # (endtime, room)
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have become available
            while occup and occup[0][0] <= start:
                _, room = heappop(occup)
                heappush(free, room)

            # Schedule the meeting in the soonest available room
            if free:
                room = heappop(free)
                heappush(occup, (end, room))
                count[room] += 1
            else:
                earlyEnd, room = heappop(occup)
                newEnd = max(earlyEnd, start) + (end - start)  # Schedule after the current earliest end
                heappush(occup, (newEnd, room))
                count[room] += 1

        # Find the room that hosted the most meetings
        maxVal = max(count)
        return count.index(maxVal)

