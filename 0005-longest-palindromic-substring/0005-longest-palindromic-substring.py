class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        memo = {}
        def isPalindrome(left, right):
          
          if (left,right) in memo:
            return memo[(left,right)]
          
          if left >= right:
            return True
          
          if s[left] != s[right]:
            return False
          
          memo[(left,right)] = isPalindrome(left+1, right-1)
          
          return memo[(left,right)]
        
        
        result = ""
        for i in range(len(s)):
          for j in range(i,len(s)):
            if len(s[i:j+1]) > len(result) and isPalindrome(i,j):
              
              result = s[i:j+1]
              
                   
        return result 
          