class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(f"{len(s)}#{s}" for s in strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            L = int(s[i:j])
            j+=1
            res.append(s[j:j+L])
            i=j+L
        return res

            

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))