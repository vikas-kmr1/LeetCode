
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(N,M,i,j):
            if( i < 0  or  j < 0 or j >= M or i >= N or grid[i][j] != 1 ):
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(N,M,i+1,j) + dfs(N,M,i-1,j) + dfs(N,M,i,j+1) + dfs(N,M,i,j-1)
        
        ans = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(n,m,i,j))
        return ans
        
        
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()

#         def dfs(r, c):
#             if (
#                 r < 0
#                 or r == ROWS
#                 or c < 0
#                 or c == COLS
#                 or grid[r][c] == 0
#                 or (r, c) in visit
#             ):
#                 return 0
#             visit.add((r, c))
#             return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

#         area = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 area = max(area, dfs(r, c))
#         return area