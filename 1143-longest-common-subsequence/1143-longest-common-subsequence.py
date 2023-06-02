class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        t1 = len(text1)
        t2 = len(text2)
        lenS = [[0 for i in range(t2+1)] for j in range(t1+1)]
        
        for i in range(t1-1, -1, -1):
          for j in range(t2-1, -1, -1):
            
            if(text1[i] == text2[j]):
              lenS[i][j] = 1 + lenS[i+1][j+1]
            else:
              lenS[i][j] = max(lenS[i][j+1], lenS[i+1][j])
              
        return lenS[0][0]