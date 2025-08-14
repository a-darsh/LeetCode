class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter = [0]*26
        for c in s:
            counter[ord(c)-ord('a')]+=1
        for c in t:
            idx = ord(c)-ord('a')
            counter[idx]-=1
            if counter[idx]<0:
                return False
        return True
        #O(N), O(1)