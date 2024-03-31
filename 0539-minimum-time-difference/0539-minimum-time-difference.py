class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        
        for i, t in enumerate(timePoints):
            hr = int(t[:2])
            mt = int(t[-2:])
            timePoints[i] = hr*60+mt
        
        timePoints = sorted(timePoints)
        l = len(timePoints)
        minDiff = (24*60-timePoints[l-1]+timePoints[0])
        i,j = 0,1    
        while(j<l):
            minDiff = min(timePoints[j]-timePoints[i], minDiff)
            i+=1
            j+=1
        
        
        return  minDiff
            