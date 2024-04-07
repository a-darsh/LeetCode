class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m,n  = len(heights), len(heights[0])
        visited = set()
        minHeap = [(0,0,0)] #diff, row, col
        
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r,c) == (m-1,n-1):
                return diff
            
            if (r,c) in visited:
                continue
            
            visited.add((r,c))
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                rd,cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and (rd,cd) not in visited:
                    newDiff = max(diff, abs(heights[r][c]-heights[rd][cd]))
                    heapq.heappush(minHeap, (newDiff, rd, cd))
        
            
            
        
            
        