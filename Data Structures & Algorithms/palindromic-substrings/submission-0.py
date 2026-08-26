class Solution:
    def countSubstrings(self, s: str) -> int:
        # start from the middle char
        # and extend outwards
        count = 0
        for i in range(len(s)):
            # oddLen 
            l = r = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1
            # even Len
            l = i
            r = l + 1    
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                l -= 1
                r += 1

        return count        

        