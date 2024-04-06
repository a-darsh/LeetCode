class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        newStr = s
        sorted_combination = sorted(zip(indices, sources, targets), reverse=True)
    
        for idx, source, target in sorted_combination:
            if s[idx:idx+len(source)]==source:
                newStr = newStr[:idx] + target + newStr[idx+len(source):]
        return newStr
            
        