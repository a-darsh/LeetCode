import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start, end = [], []
        for i,j in intervals:
            start.append(i)
            end.append(j)
        
        start.sort()
        end.sort()
        
        s, e=0,0
        rooms = 0
        minRooms = 0
        while(s<len(start)):
            if start[s] < end[e]:
                s+=1
                rooms+=1
            else:
                e+=1
                rooms-=1
            minRooms = max(minRooms, rooms)
            
        return minRooms
        
            
        
            
            