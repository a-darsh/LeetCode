class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        res = []
        going_up = True
        r,c = 0,0
        while len(res)!=row*col:
            if going_up:
                while r>=0 and c<col:
                    res.append(mat[r][c])
                    r-=1
                    c+=1
                if c==col:
                    c-=1
                    r+=2
                else:
                    r+=1
                going_up = False
            else:
                while r<row and c>=0:
                    res.append(mat[r][c])
                    r+=1
                    c-=1
                if r==row:
                    r-=1
                    c+=2
                else:
                    c+=1
                going_up = True
        
        return res

    #O(m*n), O(m*n)