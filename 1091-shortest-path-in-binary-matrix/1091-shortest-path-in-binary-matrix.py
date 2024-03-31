class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1
        
        queue = deque([(1,0,0)])
        visited = set()
        
        while(queue):
            (length, r,c) = queue.popleft()
            
            if (r,c)==(m-1,n-1):
                return length
            
            visited.add((r,c))
            for i,j in [[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1],[0,1],[0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and (rd,cd) not in visited and grid[rd][cd]==0:
                    queue.append((length+1,rd,cd))
                    visited.add((rd,cd))
            
            
        
        return -1
                    