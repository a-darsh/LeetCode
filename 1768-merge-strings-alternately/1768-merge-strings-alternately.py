class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        mstr = ''
        
        if len(word1) > len(word2):
          for i in range(len(word2)):
            mstr = mstr + word1[i] + word2[i]
            
          mstr = mstr + word1[len(word2):]
          
        else:
          for i in range(len(word1)):
            mstr = mstr + word1[i] + word2[i]
            
          mstr = mstr + word2[len(word1):]
          
        return mstr
            
          