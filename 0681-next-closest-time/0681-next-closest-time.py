class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        allowed = {int(i) for i in time if i!=':'}
        cur = int(time[:2])*60 + int(time[3:])
        print(cur)
        
        while True:
            cur = (cur+1)%(24*60)
            hh, mm = divmod(cur, 60)
            hh = f"{hh:02}"
            mm =f"{mm:02}"
            if all(int(i) in allowed for i in hh+mm):
                return hh+":"+mm
            
        
        
        
        
        