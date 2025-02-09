class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removeIndx = set()
        for i,c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            else:
                if not stack:
                    removeIndx.add(i)
                else:
                    stack.pop()
        removeIndx = removeIndx.union(set(stack))
        res = []
        for i,c in enumerate(s):
            if i not in removeIndx:
                res.append(c)
        return ''.join(res)
        # O(N), O(N)