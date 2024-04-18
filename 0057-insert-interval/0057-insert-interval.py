class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort()
        l,r = 0, len(intervals)-1
        while(l<=r):
            mid = (l+r)//2
            if intervals[mid][0]>=newInterval[0]:
                r=mid-1
            else:
                l=mid+1
        intervals.insert(l, newInterval)
        merged = []
        for start,end in intervals:
            if merged and merged[-1][1]>=start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged