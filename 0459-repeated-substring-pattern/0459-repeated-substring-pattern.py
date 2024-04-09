class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        l = len(s)
        
        if l==1:
            return False
        
        for i in range(1, l//2+1):
            if s==s[:i]*(l//i):
                return True
        
        return False
