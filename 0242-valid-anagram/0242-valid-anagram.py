class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
          return False
        
        hmap1 = {}
        hmap2 = {}
        
        for c in s:
          if c in hmap1:
            hmap1[c] += 1
          else:
            hmap1[c] = 1
            
        for c in t:
          if c in hmap2:
            hmap2[c] += 1
          else:
            hmap2[c] = 1
            
        for k,v in hmap1.items():
          if k not in hmap2 or hmap2[k] != v:
            return False
          
        return True