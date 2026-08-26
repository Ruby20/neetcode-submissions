class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            str_len = len(s)
            res.append(str(str_len))
            res.append("#") # delimiter
            res.append(s)

        return "".join(res)    # output is a str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # 4DelimStr
            while s[j] != "#":
                j += 1
            slen = int(s[i:j])
            i = j + 1 
            j = i + slen
            res.append(s[i:j])
            i = j
        
        return res    

