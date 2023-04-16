class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if (len(t) != len(s)) :
        return False
      for val in s:
        if val in t:
          t = t.replace(val,'',1)
          continue
        else:
          return False
      return True
        
        