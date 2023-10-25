class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dps(s):
          if s in memo:
            return memo[s]

          if s == "":
            return True

          for w in wordDict:
            if s.startswith(w):
              rem = s[len(w):]
              print(s, rem)
              if dps(rem):
                memo[rem] = True
                return True
          
          memo[s] = False
          return False
        
        return dps(s)