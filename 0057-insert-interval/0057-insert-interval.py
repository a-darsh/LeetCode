class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        l,r = 0, len(intervals)-1
        while(l<=r):
            mid = (l+r)//2
            if intervals[mid][0]<newInterval[0]:
                l = mid+1
            else:
                r = mid-1
        
        intervals.insert(l, newInterval)
        
        merged = []
        for interval in intervals:
            if merged and merged[-1][1]>=interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged