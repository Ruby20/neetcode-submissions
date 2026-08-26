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
        def dfs(i, node):
            if i == len(word):
                return node.isEnd

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

            if word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])    
            return False    

        return dfs(0, self.root)    


        
