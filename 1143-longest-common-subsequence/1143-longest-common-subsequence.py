class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        m, n = len(t1), len(t2)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i,j in product(range(0,m),range(0,n)):
            if t1[i] == t2[j] :
                dp[i+1][j+1] = dp[i][j] + 1 
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[m][n]

            
