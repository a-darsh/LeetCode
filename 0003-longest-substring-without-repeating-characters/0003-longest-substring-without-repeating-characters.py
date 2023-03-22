class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      mp ={}
      mlen = 0
      start = 0
      for current,c in enumerate(s):
        if c in mp:
          start = max(mp[c],start)
          
        mlen = max(mlen, current-start+1)
        mp[c] = current + 1
      return mlen
          