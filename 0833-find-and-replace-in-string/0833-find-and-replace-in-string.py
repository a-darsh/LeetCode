class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        newStr = s
        sortedComb = sorted(zip(indices, sources, targets), reverse=True)
        for idx, source, target in sortedComb:
            if s[idx:idx+len(source)]==source:
                newStr = newStr[:idx]+target+newStr[idx+len(source):]
        return newStr
            
        