class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxH = -1
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i]>maxH:
                res.append(i)
            maxH = max(maxH, heights[i])
        res.reverse()
        return res

        #O(N), O(N)