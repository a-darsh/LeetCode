class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =  0
        freqList = [0]*26
        res = 0
        maxfreq = 0
        for r in range(len(s)):
            freqList[ord(s[r])-ord('A')]+=1
            maxfreq = max(maxfreq, freqList[ord(s[r])-ord('A')])
            windLen = r-l+1
            replaceLen = windLen - maxfreq
            if replaceLen<=k:
                res = max(res, windLen)
            else:
                freqList[ord(s[l])-ord('A')]-=1
                l+=1
        return res




