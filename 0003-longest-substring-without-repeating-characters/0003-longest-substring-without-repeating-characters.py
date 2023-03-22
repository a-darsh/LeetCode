class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        maxlen =0
        start = 0
        for i,c in enumerate(s):
          while(c in substr):
            substr.remove(s[start])
            start +=1
          substr.add(c)
          maxlen = max(maxlen, i-start+1)
        return maxlen
        
          