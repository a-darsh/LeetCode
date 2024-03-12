class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []

        pmap, smap = {}, {}
        for idx in range(len(p)):
            pmap[p[idx]] = pmap.get(p[idx],0) + 1
            smap[s[idx]] = smap.get(s[idx],0) + 1
            
        ans = []
        i,j = 0, len(p)-1
        while(j<len(s)):
            flag=True
            for c in pmap:
                if pmap[c]!=smap.get(c,0):
                    flag = False
                    break
            if flag:
                ans.append(i)
            smap[s[i]] -= 1
            i+=1
            j+=1
            if j==len(s):
                break
            smap[s[j]] = smap.get(s[j], 0) + 1

        
        return ans
        
        