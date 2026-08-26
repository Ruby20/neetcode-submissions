class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS shortest path faster algo
        prices = [float("inf")] * n
        prices[src] = 0

        # build an adj list
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])

        q = deque()
        q.append([0, src, 0])

        while q:
            cost, node, stops = q.popleft()

            if stops > k:
                continue

            for nei, cst in adj[node]:    
                new_cost = cost + cst
                if new_cost < prices[nei]:
                    prices[nei] = new_cost
                    q.append([new_cost, nei, stops + 1])

        return prices[dst] if prices[dst] != float("inf") else -1