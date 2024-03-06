from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        graph = defaultdict(list)
        
        for i, j in similarPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(w, target, visited):
            if w == target:
                return True
            visited.add(w)
            for neigh in graph[w]:
                if neigh not in visited:
                    if dfs(neigh, target, visited):
                        return True
            return False
        
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                visited = set()  # Use a new visit set for each DFS call
                if not dfs(sentence1[i], sentence2[i], visited):
                    return False
        
        return True
