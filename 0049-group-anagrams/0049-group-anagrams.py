class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)
        for w in strs:
            cnt = [0]*26
            for c in w:
                cnt[ord(c)-ord('a')]+=1
            groupMap[tuple(cnt)].append(w)
        return [groupMap[g] for g in groupMap]
        #O(NK), O(NK)