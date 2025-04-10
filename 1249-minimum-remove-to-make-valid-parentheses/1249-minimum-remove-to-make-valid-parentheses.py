class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i, c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    remove.add(i)
        remove = remove.union(set(stack))
        temp = []
        for i,c in enumerate(s):
            if i not in remove:
                temp.append(s[i])
        return ''.join(temp)

        #O(N), O(N)
