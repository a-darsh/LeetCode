class Solution:
    def isValid(self, s: str) -> bool:
        stck =  []
        mapp = {'(':')', '{':'}', '[':']'}
        
        for c in s:
          if c in mapp:
            stck.append(c)
          else:
            if stck and mapp[stck[-1]] == c:
              stck.pop()
            else:
              return False
        return False if stck else True
          