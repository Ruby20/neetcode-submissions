class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # seems like the variant of can concatenate DP I saw on structy
        memo = {}

        def dfs(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]    

            for word in wordDict:
                if s.startswith(word):
                    suffix = s[len(word): ]
                    if dfs(suffix):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return dfs(s)                


        
        