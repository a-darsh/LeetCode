class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hmap = {}
        for c in chars:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1
        print(hmap)
        ans = 0
        for w in words:
            check=True
            for c in w:
                if c not in hmap or w.count(c)>hmap[c]:  
                    check=False
            
            if check:
                ans+=len(w)
        
        return ans