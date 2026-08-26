class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        parent = [i for i in range(n)]    
        rank =[1] * n

        def find(n1):
            res = n1

            while res != parent[res]:
                parent[res] = parent[parent[res]] # path compression
                res = parent[res]
            return res    

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n  
        for n1,n2 in edges:
            res -= union(n1, n2)

        return res    







        # union Find Algorithm
        # or dfs algo
        # def iterative_dfs(graph, start_node):
        #     visited = set()
        #     stack = [start_node]

        #     while stack:
        #         node = stack.pop()
        #         if node not in visited:
        #             visited.add(node)
        #             # Add neighbors to the stack
        #             for neighbor in graph[node]:
        #                 if neighbor not in visited:
        #                     stack.append(neighbor)
        #     return visited

        
