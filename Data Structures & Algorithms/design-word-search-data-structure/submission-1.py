class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True        
        
    def search(self, word: str) -> bool:

        def dfs(j, node):
            cur = node

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False        
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]   
            return cur.isEnd        
        return dfs(0, self.root)             



        
