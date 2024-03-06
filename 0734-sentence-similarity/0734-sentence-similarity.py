class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        l1, l2 = len(sentence1), len(sentence2)
        
        if l1!=l2:
            return False
        
        graph = defaultdict(list)
        for i,j in similarPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        for i in range(l1):
            if sentence1[i] != sentence2[i] and sentence2[i] not in graph[sentence1[i]]:
                return False
        
        return True
        