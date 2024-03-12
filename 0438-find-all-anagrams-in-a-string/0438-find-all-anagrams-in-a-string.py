class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []

        pmap, smap = {}, {}
        for idx in range(len(p)):
            pmap[p[idx]] = pmap.get(p[idx],0) + 1
            smap[s[idx]] = smap.get(s[idx],0) + 1
            
        ans = [0] if pmap==smap else []
        l = 0
        for i in range(len(p), len(s)):
            
            smap[s[i]]  = smap.get(s[i], 0) + 1
            smap[s[l]] -= 1
            if smap[s[l]]==0:
                smap.pop(s[l])
            
            l+=1
            
            if smap==pmap:
                ans.append(l)
        
        return ans
        
        
        