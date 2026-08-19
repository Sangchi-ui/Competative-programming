from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break
                        
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = len(words[i])
            
        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                if dp[mask][i] == float('inf'):
                    continue
                
                for j in range(n):
                    if not (mask & (1 << j)):
                        next_mask = mask | (1 << j)
                        added_len = len(words[j]) - overlap[i][j]
                        if dp[mask][i] + added_len < dp[next_mask][j]:
                            dp[next_mask][j] = dp[mask][i] + added_len
                            parent[next_mask][j] = i
                            
        full_mask = (1 << n) - 1
        min_len = float('inf')
        last_idx = -1
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last_idx = i
                
        path = []
        curr_mask = full_mask
        curr_idx = last_idx
        while curr_idx != -1:
            path.append(curr_idx)
            prev_idx = parent[curr_mask][curr_idx]
            curr_mask ^= (1 << curr_idx)
            curr_idx = prev_idx
            
        path.reverse()
        
        res = words[path[0]]
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            overlap_len = overlap[prev][curr]
            res += words[curr][overlap_len:]
            
        return res