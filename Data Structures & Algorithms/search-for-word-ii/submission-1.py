class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]         
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # hashmap with Tries/prefix trees
        root = TrieNode()

        # create a prefix trees of the words
        for w in words:
            root.addWord(w)

        # implement backtracking DFS
        rows, cols = len(board), len(board[0])
        visit = set()
        res = set()

        def dfs(r, c, word, node):
            if (min(r, c) < 0 or 
                r == rows or c == cols or
                (r, c) in visit or board[r][c] not in node.children):
                    return 

            visit.add((r, c))    
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            dfs(r + 1, c, word, node)   
            dfs(r - 1, c, word, node)  
            dfs(r , c + 1, word, node)    
            dfs(r , c - 1, word, node)    

            visit.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)

        return list(res)        
        