class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0]*(len(temperatures))
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                temp, pos = stack.pop()
                ans[pos] = (i-pos)
            stack.append((t,i))
        
        return ans