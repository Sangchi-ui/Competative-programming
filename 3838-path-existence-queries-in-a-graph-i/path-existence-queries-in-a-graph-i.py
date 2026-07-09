class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        # Connect adjacent nodes if the difference is within maxDiff
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i + 1)
                
        # Answer queries
        results = []
        for u, v in queries:
            results.append(find(u) == find(v))
            
        return results