def dfs(grid, row ,column):
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
        return 
    
    if grid[row][column] == '1':
        grid[row][column] = '#'
        dfs(grid,row+1,column)
        dfs(grid,row-1,column)
        dfs(grid,row,column+1)
        dfs(grid,row,column-1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols  = len(grid), len(grid[0])
        
        no_of_islands =  0 
        
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == '1':
                    dfs(grid,row,column)
                    no_of_islands += 1
                
                    
        return no_of_islands
        