class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ansList = []

        def dps(s, ans=[]):

            if not s:
                ansList.append(' '.join(ans))
                return

            for w in wordDict:

                if s.startswith(w):
                    # Attempt to move forward by taking the word
                    dps(s[len(w):], ans + [w])

        dps(s)
        return ansList