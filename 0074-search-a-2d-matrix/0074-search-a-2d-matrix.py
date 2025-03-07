class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row*col -1
        while (l<=r):
            mid = (l+r)//2
            ele = matrix[mid//col][mid%col]
            if target==ele:
                return True
            elif target<ele:
                r=mid-1
            else:
                l=mid+1
        return False

        # O(log(m*n)), O(1)