class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        for s in strs:
            hmap[tuple(sorted(s))].append(s)
        
        ans = []
        for k,v in hmap.items():
            ans.append(v)
        
        return ans
    
    #TC: nklog(k), SC: n
            
            
        