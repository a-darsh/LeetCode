class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        count = Counter()
        ans = float('-inf')
        for r in range(len(s)):
            count[s[r]]+=1
            while count[s[r]]>1:
                count[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans if ans!=float('-inf') else 0