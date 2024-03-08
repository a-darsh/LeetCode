class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x:x[0])
        
        for i in range(0, len(intervals)-1):
            if intervals[i][1] >intervals[i+1][0]:
                return False
        
        return True
        
        
        
        
        