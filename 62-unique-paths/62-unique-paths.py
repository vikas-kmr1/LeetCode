class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def gridTravellor(m,n,memo={}):
            key = m,n
            if key in memo:
                return memo[key]
            if m==1 and n==1:
                return 1
            if m==0 or n==0:
                return 0
            else:
                memo[key] = gridTravellor(m-1, n, memo) + gridTravellor(m, n-1, memo)
            return memo[key]
        return gridTravellor(m,n)