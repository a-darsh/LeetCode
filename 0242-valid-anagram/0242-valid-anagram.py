class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        if l1!=l2:
            return False
        counter1 = Counter(s)
        counter2 = Counter(t)
        for c in counter1:
            if c not in counter2 or counter1[c]!=counter2[c]:
                return False
        return True