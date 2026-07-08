class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        # Precompute power of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        sumD = [0] * (n + 1)
        cntN0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        for i, char in enumerate(s):
            d = int(char)
            sumD[i+1] = sumD[i] + d
            cntN0[i+1] = cntN0[i] + (1 if d > 0 else 0)
            if d > 0:
                p[i+1] = (p[i] * 10 + d) % MOD
            else:
                p[i+1] = p[i]
                
        ans = []
        for l, r in queries:
            n0 = cntN0[r+1] - cntN0[l]
            sd = sumD[r+1] - sumD[l]
            if n0 == 0:
                ans.append(0)
            else:
                # Calculate x = (p[r+1] - p[l] * 10^n0) % MOD
                x = (p[r+1] - (p[l] * pow10[n0]) % MOD + MOD) % MOD
                ans.append((x * sd) % MOD)
        return ans