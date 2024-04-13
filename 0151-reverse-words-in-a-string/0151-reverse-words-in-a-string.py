from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        
        l, r = 0, len(s)-1
        
        while l<=r and s[l]==' ':
            l+=1
        
        while l<=r and s[r]==' ':
            r-=1
            
        word=[]
        q = deque()
        while l<=r:
            if s[l]!=" ":
                word.append(s[l])
            elif word:
                q.appendleft(''.join(word))
                word=[]
            l+=1
        q.appendleft(''.join(word))
        
        return " ".join(q)
        