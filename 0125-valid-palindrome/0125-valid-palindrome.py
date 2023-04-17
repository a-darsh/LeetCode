class Solution:
    def isPalindrome(self, s: str) -> bool: 
        cleans = ""
        cleans += ''.join(c if c.isalnum() else '' for c in s)
        cleans = cleans.lower()
        i,j = 0,len(cleans)-1
        
        while(i!=j):
          
          if i >= len(cleans) or j < 0 :
            break
          
          if cleans[i] != cleans[j]:
            return False
          
          i += 1
          j -= 1 
        
        return True