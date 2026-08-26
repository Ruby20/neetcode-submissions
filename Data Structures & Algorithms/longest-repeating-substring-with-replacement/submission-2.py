class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = {}
        max_val = 0

        left = 0
        for right in range(len(s)):
            max_freq[s[right]] = 1 + max_freq.get(s[right], 0)

            window_len = right - left + 1
            max_val = max(max_val, max_freq[s[right]])

            if window_len - max_val > k:
                max_freq[s[left]] -= 1
                left += 1

        return (right - left + 1)



        