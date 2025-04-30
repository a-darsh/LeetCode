class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove  = set()
        stack = []
        for i,c in enumerate(s):
            if c =='(':
                stack.append(i)
            elif c==')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        
        remove = remove.union(set(stack))
        temp = []
        for i,c in enumerate(s):
            if i not in remove:
                temp.append(c)

        return ''.join(temp)
        
#O(N), O(N)