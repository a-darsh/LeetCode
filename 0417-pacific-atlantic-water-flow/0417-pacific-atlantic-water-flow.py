class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        pVisit, aVisit = set(), set()
        
        def dfs(r,c, visit):
            if (r,c) in visit:
                return
            visit.add((r,c))
            for d in [[1,0], [-1,0],[0,1], [0,-1]]:
                rd, cd = r+d[0], c+d[1]
                if 0<=rd<m and 0<=cd<n and (rd,cd) not in visit and heights[rd][cd]>=heights[r][c]:
                    dfs(rd,cd, visit)
        
        
        for i in range(m):
            dfs(i, 0, pVisit)
            dfs(i, n-1, aVisit)
        
        for j in range(n):
            dfs(0,j, pVisit)
            dfs(m-1, j, aVisit)
            
        return (pVisit & aVisit)
        
        