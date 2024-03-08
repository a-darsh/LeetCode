import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        stck = []
        time = []
        for i, j in intervals:
            time.append((i,'s'))
            time.append((j,'e'))
        
        time.sort()
        rooms = 0
        minRooms = 0
        while(time):
            ele = time.pop(0)[1]
            if ele=='s':
                rooms+=1
                minRooms = max(minRooms, rooms)
            elif ele=='e':
                rooms-=1
        
        return minRooms
        
            
        
            
            