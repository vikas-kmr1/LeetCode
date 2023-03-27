# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0

#         islands = 0
#         visit = set()
#         rows, cols = len(grid), len(grid[0])

#         def dfs(r, c):
#             if (
#                 r not in range(rows)
#                 or c not in range(cols)
#                 or grid[r][c] == "0"1
#                 or (r, c) in visit
#             ):
#                 return

#             visit.add((r, c))
#             directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     islands += 1
#                     dfs(r, c)
#         return islands


def dfs(grid, row ,column):
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0] or grid[row][column] != '1'):
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
        