class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u][count]:
                continue
            for v, w in adj[u]:
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1
                if new_count <= k:
                    new_d = d + w
                    if new_d < dist[v][new_count]:
                        dist[v][new_count] = new_d
                        heapq.heappush(pq, (new_d, v, new_count))
        return -1