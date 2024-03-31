class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
                
        intervals = sorted(intervals)
        i = 0
        while(i<len(intervals)-1):
            curMeeting = intervals[i]
            nxtMeeting = intervals[i+1]
            if curMeeting[1]>nxtMeeting[0]:
                return False
            i+=1
        
        return True
        
        
        
        
        