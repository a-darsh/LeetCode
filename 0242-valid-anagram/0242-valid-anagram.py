class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):
            return False
        
        hmap1, hmap2 = {}, {}
        for i in range(len(s)):
            hmap1[s[i]] = hmap1.get(s[i],0) + 1 
            hmap2[t[i]] = hmap2.get(t[i],0) + 1 
        
        for c in hmap1:
            if hmap1[c]!=hmap2.get(c):
                return False
        
        return True