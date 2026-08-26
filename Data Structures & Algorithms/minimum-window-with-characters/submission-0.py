class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        t_count = {}
        s_count = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0) # populate the t_map

        have = 0
        need = len(t_count)   # exact keys 

        left = 0
        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):
            s_count[s[right]] = 1 + s_count.get(s[right], 0)

            if s[right] in t_count and s_count[s[right]] == t_count[s[right]]:
                have += 1

            while need == have:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1   

                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left: right + 1] if resLen != float("inf") else ""            







        