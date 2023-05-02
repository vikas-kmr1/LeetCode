# from collections import deque
# class Solution:
#     def shortestPathBinaryMatrix(self,grid):
#         n = len(grid)
#         if grid[0][0] or grid[n-1][n-1]:
#             return -1
        
#         q = [(0, 0, 1)]
#         grid[0][0] = 1
        
#         while q:
#             i, j, d = q.pop(0)
            
#             if i == n-1 and j == n-1: return d
            
#             dirs = ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1))
#             for x, y in dirs:
#                 if 0 <= x < n and 0 <= y < n and not grid[x][y]:
#                     grid[x][y] = 1
#                     q.append((x, y, d+1))
#         return -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
             return -1
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()

            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in directions:
                x, y = r + dr, c + dc
                if (0 <= x < N ) and (0 <= y < N) and (grid[x][y] == 0) and ( (x,y) not in visit):
                    q.append((x, y, length + 1))
                    visit.add((x, y))
        return -1



    