class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        merged = []
        for interval in intervals:
            if merged and merged[-1][1]>=interval[0]:
                newMerge = [merged[-1][0],max(merged[-1][1],interval[1])]
                merged.pop()
                merged.append(newMerge)
            else:
                merged.append(interval)
        
        return merged
        
        
        
        
        