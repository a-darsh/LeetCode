class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        visited = set()
        def dfs(j1,j2):
            if j1+j2==target:
                return True
            if j1>x or j2>y or j1<0 or j2<0:
                return False
            visited.add((j1,j2))
            for j1d, j2d in [[x,j2], [j1,y], [j1,0], [0,j2], [j1+min(j2,x-j1),j2-min(j2,x-j1)], [j1-min(j1, y-j2), j2+min(j1, y-j2)]]:
                if (j1d,j2d) not in visited and dfs(j1d, j2d):
                    return True
            
            return False
        
        return dfs(0,0)