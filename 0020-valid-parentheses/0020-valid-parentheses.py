class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stck.append(c)
            else:
                if not stck:
                    return False  
                while stck:
                    temp = stck.pop()
                    if c==')' and temp=='(' or c=='}' and temp=='{' or  c==']' and temp=='[':
                        break
                    else:
                        return False
        if stck:
            return False
        else:
            return True