class Solution:
    def isPalindrome(self, s: str) -> bool:
      
      s = ''.join(c.lower() for c in s if c.isalnum())
      
      r = ''.join(s[i] for i in range(len(s)-1, -1, -1))
      
      return s==r
        