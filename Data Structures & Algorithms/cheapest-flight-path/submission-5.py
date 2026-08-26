class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS with Priority queue is optimal
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        dist = [[float("inf")] * (k + 4) for _ in range(n)]    

        dist[src][0] = 0
        minheap = [(0, src, -1)]

        while minheap:
            cost, node, stops = heapq.heappop(minheap)

            if node == dst:
                return cost

            if stops == k or dist[node][stops + 1] < cost:
                continue

            for nei, w in adj[node]:
                next_cost = cost + w
                next_stop = stops + 1
                if dist[nei][next_stop + 1] > next_cost:
                    dist[nei][next_stop + 1] = next_cost
                    heapq.heappush(minheap, (next_cost, nei, next_stop))
        
        return -1

