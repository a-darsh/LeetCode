class Solution:
    def isValid(self, s: str) -> bool:
        stck =  []
        
        for c in s:
          if c in ['(','{','[']:
            stck.append(c)
          else:
            if stck:
              if ( (stck[-1] == '(' and c!=')') 
              or (stck[-1] == '{' and c!='}') 
              or (stck[-1] == '[' and c!=']') ):
                return False
              stck.pop()
            else:
              return False
        
        if stck:
          return False
        
        return True
          