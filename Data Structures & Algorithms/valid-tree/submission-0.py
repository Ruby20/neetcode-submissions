class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid Tree
        #. no loops
        #. connected edges

        # hashmap
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)    

        cycle = set()

        def dfs(cur, prev):
            if cur in cycle:
                return False

            cycle.add(cur)
            for j in adj[cur]:
                if j == prev:
                    continue
                if not dfs(j, cur):
                    return False
            return True

        return dfs(0, -1) and n == len(cycle)

        