class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for c in s:
          
          if c == '(' or c=='[' or c=='{':
            stck.append(c)
            
          elif stck:
            k = stck.pop()
            if (c == ')' and k != '(') or (c == ']' and k != '[') or (c == '}' and k != '{'):
              return False
            
          else:
            return False
            
        if not stck:
          return True
        return False