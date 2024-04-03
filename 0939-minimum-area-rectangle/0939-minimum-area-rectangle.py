class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        visited = set()
        minArea = float('inf')
        
        for x1,y1 in points:
            for x2,y2 in visited:
                if (x1,y2) in visited and (x2,y1) in visited:
                    minArea  = min((abs(x1-x2) * abs(y1-y2)), minArea)
            visited.add((x1,y1))
        
        return minArea if minArea!=float('inf') else 0
            
            