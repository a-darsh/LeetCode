class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter()
        for c in magazine:
            count[c]+=1
        for c in ransomNote:
            if c not in count:
                return False
            count[c]-=1
            if not count[c]:
                del count[c]
        return True