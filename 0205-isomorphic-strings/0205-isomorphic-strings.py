class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        st = {}
        ts = {}
        for c1,c2 in zip(s,t):
            if c1 not in st and c2 not in ts:
                st[c1] = c2
                ts[c2] = c1
            if c1 in st and st[c1]!=c2:
                return False
            if c2 in ts and ts[c2]!=c1:
                return False
        return True
                
                
                
                