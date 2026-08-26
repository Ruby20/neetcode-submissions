class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#str should be prefixlength encoding pattern we use here
        res = []
        for s in strs:
            slen = len(s)
            res.append(str(slen))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # two pointers
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            slen = int(s[i:j])
            i = j + 1
            j = i + slen
            word = s[i:j]    
            res.append(word)
            i = j

        return res
