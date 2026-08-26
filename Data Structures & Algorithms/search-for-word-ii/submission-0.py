class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word): # O(1)
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]        
        cur.isWord = True    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.insert(w)

        rows, cols = len(board), len(board[0])
        path = set()
        res = set()
        # backtracking DFS
        def dfs(r, c, node, word):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] not in node.children
                or (r, c) in path):
                return

            path.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word) 
            path.remove((r, c))  

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)            









        