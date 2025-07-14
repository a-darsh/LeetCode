class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [False]*128
        res = 0
        l,r= 0,0
        for r in range(len(s)):
            while seen[ord(s[r])]:
                seen[ord(s[l])] = False
                l+=1
            seen[ord(s[r])] = True
            res = max(res, r-l+1)
        return res

        #O(N), O(1)
