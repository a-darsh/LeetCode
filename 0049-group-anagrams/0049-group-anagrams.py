class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in hmap:
                hmap[temp] = [s]
            else:
                hmap[temp].append(s)
        return hmap.values()
        
        
            