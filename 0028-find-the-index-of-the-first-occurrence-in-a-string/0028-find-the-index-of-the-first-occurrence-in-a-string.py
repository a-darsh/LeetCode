class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i, j = 0, len(needle)-1
        while(j<len(haystack)):
            check = True
            for k in range(i, j+1):
                if needle[k-i]!=haystack[k]:
                    check=False
            if check:
                return i
            i+=1
            j+=1
            
        
        return -1
        