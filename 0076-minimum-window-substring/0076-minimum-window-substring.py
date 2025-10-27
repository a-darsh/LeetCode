from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        best_left = 0
        best_len = float('inf')

        for right, ch in enumerate(s):
            if need[ch]>0:
                missing-=1
            need[ch]-=1
            
            while missing==0:
                if right-left+1<best_len:
                    best_len = right-left+1
                    best_left = left

                left_ch = s[left]
                need[left_ch]+=1
                if need[left_ch]>0:
                    missing+=1
                left+=1
        return "" if best_len==float('inf') else s[best_left:best_left+best_len]
        #O(m+n), O(m)