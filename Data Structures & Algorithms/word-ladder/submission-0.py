class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph problem
        # BFS - shortest path of transformation
        # set and queue are the DS
        # Patterns we are going to store in the adj list
            # hot -> h * t, * o t, h o *

        if endWord not in wordList or beginWord == endWord:
            return 0    

        q = deque([beginWord])
        visit = set([beginWord])
        adj_list = collections.defaultdict(list)

        # word list does not have the begin word
        wordList.append(beginWord)
        res = 1

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1: ]
                adj_list[pattern].append(word)
    
        # print(adj_list)
        # BFS
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1: ] # key
                    for wd in adj_list[pattern]:
                        if wd not in visit:
                            visit.add(wd)
                            q.append(wd)
            res += 1        
        return 0        

        