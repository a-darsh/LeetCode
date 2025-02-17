class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = defaultdict(int)
        for c in s:
            hmap[c]+=1
        
        res = []
        for c in order:
            if c in hmap:
                res.extend(c*hmap[c])
                del hmap[c]
        for c in hmap:
            res.extend(c*hmap[c])
        return ''.join(res)
        
