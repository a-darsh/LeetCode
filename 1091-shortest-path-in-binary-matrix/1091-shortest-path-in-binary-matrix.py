class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N=len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        
        q=collections.deque([(0,0,1)])
        while q:
            r,c,length = q.popleft()
            if r==N-1 and c==N-1:
                return length
            for i,j in [[1,0], [-1,0], [0,1], [0, -1], [1,1], [-1,1], [1,-1], [-1,-1]]:
                row,col = r+i, c+j
                if 0<=row<N and 0<=col<N and not grid[row][col]:
                    q.append((row,col,length+1))
                    grid[row][col]=1
        return -1