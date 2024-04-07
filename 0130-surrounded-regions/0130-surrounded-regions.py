class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n  = len(board), len(board[0])
        visited = set()
        
        def dfs(r,c):
            if (r,c) in visited:
                return 
            if board[r][c]!='O':
                return
            visited.add((r,c))
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                rd, cd = r+i, c+j
                if 0<=rd<m and 0<=cd<n and (rd,cd) not in visited and board[rd][cd]=='O':
                    dfs(rd,cd)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=='O' and (i,j) not in visited:
                    board[i][j]='X'
        
        