class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1>n2:
            return False

        need, window = [0]*26, [0]*26
        base = ord('a')
        for c in s1:
            need[ord(c)-base]+=1
        
        # First window check
        left, right = 0, n1
        for c in s2[left:right]:
            window[ord(c)-base]+=1
        if need==window:
            return True
        
        # Sliding window
        while right<n2:
            window[ord(s2[left])-base]-=1
            window[ord(s2[right])-base]+=1
            left+=1
            right+=1
            if need==window:
                return True
        return False

        # O(n1+n2), O(1)