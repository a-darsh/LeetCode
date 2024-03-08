class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        time = []
        for i,j in intervals:
            time.append([i,'s'])
            time.append([j,'e'])
        
        time.sort()
        
        for t in range(0, len(time)-1):
            if time[t][1]==time[t+1][1]:
                return False
        
        return True
        
        
        
        