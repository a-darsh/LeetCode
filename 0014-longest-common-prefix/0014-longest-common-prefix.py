class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        for i in range(len(strs[0])):
            c=strs[0][i]
            check =True            
            for s in strs[1:]:
                if i==len(s) or s[i]!=c:
                    check=False
                    break
            if not check:
                break
        
            ans += c
            
        return ans
                