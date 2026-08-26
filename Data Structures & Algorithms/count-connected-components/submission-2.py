class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)            

        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False     

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res        
        