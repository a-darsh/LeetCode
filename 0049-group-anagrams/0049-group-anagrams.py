class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)
        for word in strs:
            groupMap[''.join(sorted(word))].append(word)
        res = []
        for group in groupMap:
            res.append(groupMap[group])
        return res