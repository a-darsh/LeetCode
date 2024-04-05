class Solution:
    def countTime(self, time: str) -> int:
        
        count = 0
        for i in range(1440):
            hh = i//60
            mm = i%60
            validTime = f"{hh:02}:{mm:02}"
            good = True
            for a,b in zip(time, validTime):
                if a!=b and a!='?':
                    good=False
                    break
            if good:
                count+=1
        return count
            
        
        
        