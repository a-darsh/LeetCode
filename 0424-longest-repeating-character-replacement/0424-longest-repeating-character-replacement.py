class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        freqMap={}
        l,r = 0,0 
        while r<len(s):
            freqMap[s[r]] = 1 + freqMap.get(s[r],0)
            if r-l+1 - max(freqMap.values()) <= k:
                if r-l+1 > ans:
                    ans = r-l+1
            else:
                freqMap[s[l]]-=1
                l+=1
            r+=1
        
        return ans