class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        hmap1, hmap2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            hmap1[s[i]]+=1
            hmap2[t[i]]+=1
        for k,v in hmap1.items():
            if v!=hmap2[k]:
                return False
        return True