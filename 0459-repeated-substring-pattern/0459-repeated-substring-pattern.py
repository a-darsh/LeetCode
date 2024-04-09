class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        l = len(s)
        if l == 1:
            return False
        
        for i in range(1, l//2 + 1):  # Start from 1 and go up to l//2
            if l % (i) == 0:  # Check if the length of s is divisible by i
                if s == (s[:i]) * (l//i):
                    return True
        
        return False
