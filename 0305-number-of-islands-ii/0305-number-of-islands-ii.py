class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
           
        rank, parent = {}, {}
        
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX==rootY:
                return 0
            
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
                
            return 1
        
        ansList = []
        posSet = set()
        
        ans = 0
        for i,j in positions:
            posSet.add((i,j))
            if (i,j) not in parent:
                parent[(i,j)] = (i,j)
                rank[(i,j)] = 0
                ans += 1
                for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                    r,c = i+di, j+dj
                    if (r,c) in parent:
                        if union((i,j), (r,c)):
                            ans -= 1
            ansList.append(ans)
        
        return ansList
                        
                    
                
        
        
        
            