class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        cur_seq = set()
        for right in range(len(s)):
            while s[right] in cur_seq:
                cur_seq.remove(s[left])
                left+=1
            cur_seq.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len
        #O(N), O(1)