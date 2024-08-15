# DP Question
# For any [1, 2, ... i] having j inverse pairs, suppose the last element is k, than [1, 2, ... k-1, k+1, k+2, ... i] + [k]
# f[i][j] = inverse pairs k created with the i-1 numbers (P1) & inverse pairs already exists in i-1 numbers (P2)
# For P1, # = i-k; for P2, <=> f[i-1][j-(i-k)]
# Thus, f[i][j] = sum_(k=1)^(i)(f[i-1][j-(i-k)]), where f[0][0] = 0
# Optimization: f[i][j] = f[i][j−1] − f[i−1][j−i] + f[i−1][j]

class Solution:
    def kInversePairs(self, n, k):
        mod = 10**9 + 7
        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
                g[j] %= mod
            f = g
        return f[k]

n = 4
k = 3

print(Solution.kInversePairs(Solution(), n, k))