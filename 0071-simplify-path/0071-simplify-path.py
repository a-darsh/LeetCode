class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p=='.' or not p:
                continue
            elif p=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)

        #O(n), O(n)