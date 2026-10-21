class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        s_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            s_len = max(s_len, right - left + 1)    


        return s_len