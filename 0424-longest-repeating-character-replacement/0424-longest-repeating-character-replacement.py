class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur_freq = [0]*26
        cur_max_freq = 0
        res, left, wind_len = 0, 0, 0
        for right in range(len(s)):
            cur_freq[ord(s[right])-ord('A')]+=1
            cur_max_freq = max(cur_max_freq, cur_freq[ord(s[right])-ord('A')])
            wind_len = right-left+1
            if wind_len-cur_max_freq<=k:
                res = max(res, wind_len)
            else:
                cur_freq[ord(s[left])-ord('A')]-=1
                left+=1
        return res
        #O(N), O(1)
