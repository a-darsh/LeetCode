class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(i,j):
            while(i<j):
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        i,j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return palindrome(i,j-1) or palindrome(i+1,j)
            i+=1
            j-=1
        return True