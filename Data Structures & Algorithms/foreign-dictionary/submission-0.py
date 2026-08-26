class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # input is sorted - Very important
        # for every pair of words, we find the first differing char
        # can do a DFS or BFS
        # input list - contains words that are sorted
        # output - Derive the order of letters in this language
        adj = {ch: set() for word in words for ch in word}

        # do a post order DFS
        # then reverse the final output str
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return "" # invalid
            for j in range(minlen): # intersection of these chars
                if w1[j] != w2[j]:
                   adj[w1[j]].add(w2[j])
                   break 

        visited = {} # False: visited, True:current path
        res = [] # reverse list

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)

        for c in adj:
            if dfs(c):
                return ""

        return "".join(res[::-1])        





        