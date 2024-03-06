class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        l1, l2 = len(sentence1), len(sentence2)
        
        if l1 != l2:
            return False
        
        graph = defaultdict(list)
        
        for i,j in similarPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        visit = set()
        def dfs(w, target):
            if w==target:
                return True
            visit.add(w)
            for neigh in graph[w]:
                if neigh not in visit:
                    if dfs(neigh, target):
                        visit.remove(w)
                        return True
                        
            visit.remove(w)
            return False
        
        
        for i in range(l1):
            if sentence1[i]!=sentence2[i] and not dfs(sentence1[i], sentence2[i]):
                return False
        
        return True
        