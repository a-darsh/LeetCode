class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo = {}

        def dfs(s):
            # If the current substring has been processed before, return the memoized result
            if s in memo:
                return memo[s]

            # If the current substring is empty, return a list with an empty sentence
            if not s:
                return [""]

            sentences = []

            for w in wordDict:
                if s.startswith(w):
                    # Recursive call on the remaining part of the substring after removing the word w
                    for sentence in dfs(s[len(w):]):
                        if sentence:
                            sentences.append(w + " " + sentence)
                        else:
                            sentences.append(w)

            # Memoize the result for the current substring and return
            memo[s] = sentences
            return sentences

        return dfs(s)