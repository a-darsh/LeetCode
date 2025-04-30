class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(s, i, j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        i,j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return palindrome(s, i+1, j) or palindrome(s, i, j-1)
            i+=1
            j-=1
        return True

        #O(N), O(1)