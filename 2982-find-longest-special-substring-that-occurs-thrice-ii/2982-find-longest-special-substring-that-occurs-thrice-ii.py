class Solution:
    def maximumLength(self, s: str) -> int:
        
        
        maxLengths = [1]*len(s)
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                maxLengths[i] = maxLengths[i-1]+1
        
        groups = {}
        for i in range(len(s)):
            if s[i] not in groups:
                groups[s[i]] = []
            groups[s[i]].append(maxLengths[i])
        
        ans = ''
        for k,val in groups.items():
            val.sort(reverse=True)
            if len(val)>=3 and len(k*val[2])>len(ans):
                ans = k*val[2]
                    
        return -1 if ans=='' else len(ans)        
        