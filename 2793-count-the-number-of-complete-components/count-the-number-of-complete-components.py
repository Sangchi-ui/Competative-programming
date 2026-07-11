from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
 
                component = []
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    u = queue.popleft()
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)
                            
                v_count = len(component)
                e_count = 0
                for node in component:
                    e_count += len(adj[node])
                e_count //= 2
                
                if e_count == (v_count * (v_count - 1)) // 2:
                    complete_components += 1
                    
        return complete_components