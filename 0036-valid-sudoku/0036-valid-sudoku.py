class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val!='.':
                    row = (val, r, 'r')
                    col = (val, c, 'c')
                    box = (val, (r//3,c//3), 'b')
                    if row in seen or col in seen or box in seen:
                        return False
                    seen.update([row,col,box])
        return True
        #O(1), O(1)