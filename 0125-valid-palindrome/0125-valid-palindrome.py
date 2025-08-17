class Solution:
    def isPalindrome(self, s: str) -> bool:
        checkStr = "".join(c.lower() for c in s if c.isalnum())
        i,j=0, len(checkStr)-1
        while i<j:
            if checkStr[i]!=checkStr[j]:
                return False
            i+=1
            j-=1
        return True
        #O(N), O(N)