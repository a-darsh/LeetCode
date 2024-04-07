class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        maxHeap = [(-grid[0][0],0,0)] #minimum val, row, col
        
        while maxHeap:
            val, r, c  = heapq.heappop(maxHeap)
            val = -val
            if (r,c)==(m-1,n-1):
                return val
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for i, j in [[1,0],[-1,0], [0,1],[0,-1]]:
                rd,cd = r+i,c+j
                if 0<=rd<m and 0<=cd<n and (rd,cd) not in visited:
                    newVal = min(val, grid[rd][cd])
                    heapq.heappush(maxHeap, (-newVal, rd,cd))
        
            