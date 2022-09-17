class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range( m - 1 ):
            newRow = [1]*n
            for j in range(n - 2 , -1 , -1 ) :
                newRow[ j ] = newRow[ j + 1 ] + row[ j ]
            row = newRow
        return row[0]
        # def gridTravellor(m,n,memo={}):
        #     key = m,n
        #     if memo.get(key):
        #         return memo[key]
        #     if m==1 and n==1:
        #         return 1
        #     if m==0 or n==0:
        #         return 0
        #     else:
        #         memo[key] = gridTravellor(m-1, n, memo) + gridTravellor(m, n-1, memo)
        #     return memo[key]
        # return gridTravellor(m,n)