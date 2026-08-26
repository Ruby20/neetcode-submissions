class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            res = max(res, r-l+1)
        return res    