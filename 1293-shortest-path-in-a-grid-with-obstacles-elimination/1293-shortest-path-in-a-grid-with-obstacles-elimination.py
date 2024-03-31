class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m,n  = len(grid), len(grid[0])
        visited = set()
        
        queue = deque([(0,k,0,0)]) #steps,obstacle-remain, row, column
        target = (m-1,n-1)
        
        while queue:
            
            steps,obst, r,c  = queue.popleft() 
            if (r,c)==target:
                return steps
            
            visited.add((obst,r,c))
            for i,j in [[1,0], [-1,0], [0,1], [0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n:
                    if grid[rd][cd]==1 and obst >0 and (obst-1,rd,cd) not in visited:
                        visited.add((obst-1,rd,cd))
                        queue.append((steps+1, obst-1, rd, cd))
                    elif grid[rd][cd]!=1 and (obst,rd,cd) not in visited:
                        visited.add((obst,rd,cd))
                        queue.append((steps+1, obst, rd, cd))
            
        return -1
            
            
        
        
        
            