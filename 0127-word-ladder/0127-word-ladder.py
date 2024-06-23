class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adjList = defaultdict(list)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
        
        queue = deque([(beginWord,1)])
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word==endWord:
                return level
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                for nei in adjList[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, level+1))
        
        return 0
                
        