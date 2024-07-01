class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set() #obst, row, col
        queue = deque([(0,k,0,0)]) #steps, rem obst, row, col
        visited.add((0,0,0))
        while queue:
            steps, obst, r, c = queue.popleft()
            if (r,c)==(m-1,n-1):
                return steps
            for rd, cd in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc = r+rd, c+cd
                if 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc]==1 and obst>0 and (obst-1, nr,nc) not in visited:
                        visited.add((obst-1, nr,nc))
                        queue.append((steps+1, obst-1, nr,nc))
                    if grid[nr][nc]!=1 and (obst, nr,nc) not in visited:
                        visited.add((obst, nr,nc))
                        queue.append((steps+1, obst, nr,nc))
        return -1
         
            
        
        
        
            