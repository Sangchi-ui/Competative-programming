class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted([(num, i) for i, num in enumerate(nums)])
        
        pos = [0] * n
        for sorted_idx, (num, orig_idx) in enumerate(arr):
            pos[orig_idx] = sorted_idx
            
        LOG = 18
        st = [[0] * LOG for _ in range(n)]
        
        right = 0
        for i in range(n):
            while right < n and arr[right][0] - arr[i][0] <= maxDiff:
                right += 1
            st[i][0] = right - 1
            
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            a = pos[u]
            b = pos[v]
            
            if a > b:
                a, b = b, a
                
            curr = a
            steps = 0
            
            for k in range(LOG - 1, -1, -1):
                if st[curr][k] < b:
                    curr = st[curr][k]
                    steps += 1 << k
                    
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans