class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur_freq = [0]*26
        cur_max_freq = 0
        res, l = 0, 0 
        for r,c in enumerate(s):
            cur_freq[ord(c)-ord('A')]+=1
            cur_max_freq = max(cur_max_freq, cur_freq[ord(c)-ord('A')])
            wind_len = r-l+1
            if wind_len-cur_max_freq<=k:
                res = max(res, wind_len)
            else:
                cur_freq[ord(s[l])-ord('A')]-=1
                l+=1
        return res
        #O(N), O(1)
