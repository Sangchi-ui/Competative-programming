class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """:type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods reachable from k
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
                    
        # Step 2: Check if any non-suspicious method invokes a suspicious method
        is_valid_to_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                is_valid_to_remove = False
                break
                
        # Step 3: Return remaining methods
        if is_valid_to_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))