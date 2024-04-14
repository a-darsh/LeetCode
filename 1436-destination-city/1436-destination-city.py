class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        hmap = {}
        for path in paths:
            hmap[path[0]] = path[1]
        
        for d in hmap.values():
            if d not in hmap:
                return d