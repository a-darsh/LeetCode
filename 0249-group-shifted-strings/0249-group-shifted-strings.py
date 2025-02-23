class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for s in strings:
            temp = []
            i,j = 0,1
            while j<len(s):
                temp.append((ord(s[j])-ord(s[i]))%26)
                i+=1
                j+=1
            groupDict[tuple(temp)].append(s)
        return [v for v in groupDict.values()]

        #O(N*M), O(N*M)