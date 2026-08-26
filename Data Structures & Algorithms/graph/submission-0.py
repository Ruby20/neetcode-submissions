class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()  
        self.adj_list[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        if src in self.adj_list:
            self.adj_list[src].remove(dst)
            return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self._dfs(src, dst, visit)


    def _bfs(self, src, dst, visit) -> bool:
        que = deque([src])

        while que:
            cur = que.popleft()
            if cur == dst:
                return True
            visit.add(cur)    
            for neighbor in self.adj_list.get(cur, []):
                if neighbor not in visit:
                    que.append(neighbor)
                    visit.add(neighbor)
        return False        
        
                 

    def _dfs(self, src, dst, visit) -> bool:
        if src == dst:
            return True
        visit.add(src)
        
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visit:
                if self._dfs(neighbor, dst, visit):
                    return True
        return False            












