class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        t_count = {}
        s_count = {}
        res = [-1, -1]
        resLen = float('inf')

        for i in range(len(t)):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
          
        need = len(t_count)
        have = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            s_count[s[right]] = 1 + s_count.get(s[right], 0)

            if c in t_count and s_count[c] == t_count[c]:
                have += 1

            while need == have:
                if resLen > right - left + 1:
                    resLen = right - left + 1
                    res = [left, right]

                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ''