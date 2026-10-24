class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # prefix length encoding
            # hello -> 4#hello
        res = []
        for word in strs:
            word_len = len(word)
            res.append(str(word_len))
            res.append("#")
            res.append(word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wlen = int(s[i:j])
            i = j + 1
            j = i + wlen
            res.append(s[i:j])
            i = j
        return res    
