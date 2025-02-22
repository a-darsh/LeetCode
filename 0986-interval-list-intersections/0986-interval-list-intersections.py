class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0, 0
        while i<len(firstList) and j<len(secondList):
            start1, end1 = firstList[i][0], firstList[i][1]
            start2, end2 = secondList[j][0], secondList[j][1]
            if start1>end2:
                j+=1
            elif start2>end1:
                i+=1
            else:
                res.append([max(start1, start2), min(end1, end2)])
                if end1>end2:
                    j+=1
                else:
                    i+=1
        return res

        #O(N), O(N)