class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_counter, close_counter = 0,0
        for c in s:
            if c=='(':
                open_counter+=1
            elif c==')':
                if open_counter>0:
                    open_counter-=1
                else:
                    close_counter+=1
        return open_counter+close_counter

        #O(N), O(1)
