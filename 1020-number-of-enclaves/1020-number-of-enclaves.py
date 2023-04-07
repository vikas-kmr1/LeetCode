class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r,c+1) +  dfs(r-1,c) +  dfs(r,c-1)
        
        
        #check ar border coordinates first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1) and ( i in [0 ,len(grid ) - 1 ] or j in [0 ,len(grid[0])  - 1]):
                    dfs(i,j)
                    
        print(grid)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += dfs(i,j)
        return ans