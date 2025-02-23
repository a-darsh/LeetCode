class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        prevT = -1
        for log in logs:
            funcId, check, t = log.split(":")
            funcId = int(funcId)
            t = int(t)
            if check=="start":
                if stack:
                    res[stack[-1]]+=t-prevT
                stack.append(funcId)
                prevT=t
            else:
                res[stack.pop()]+=t-prevT+1
                prevT=t+1
        return res

        #O(N), O(N)