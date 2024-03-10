class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time = 0
        good = 0
        queue = deque()
        m,n  = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        count=0
        while(queue and count !=good):
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    row, col = r+dr, c+dc
                    if 0<=row<m and 0<=col<n and grid[row][col]==1:
                        grid[row][col] = 2
                        count += 1
                        queue.append((row,col))
            
            time += 1
        
        return time if count==good else -1
                        
        