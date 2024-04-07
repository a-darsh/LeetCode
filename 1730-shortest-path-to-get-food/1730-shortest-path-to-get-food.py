class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="*":
                    start = (i,j)
                    break
            if start:
                break
        
        
        minHeap = [(0,start[0],start[1])] #dist travelled, row, col
        visited = set()
        while minHeap:
            dist, r, c = heapq.heappop(minHeap)
            if grid[r][c]=="#":
                return dist
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and grid[rd][cd]!='X' and (rd,cd) not in visited:
                    heapq.heappush(minHeap, (dist+1, rd, cd))
        
        return -1
            
        
        