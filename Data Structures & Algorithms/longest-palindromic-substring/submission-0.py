class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # the idea is to find the middle char and move to the left and right side
        for i in range(len(s)):
            l = r = i
            # odd Length
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # even length    
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
        