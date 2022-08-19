class Solution:
#Explore like a dfs
#Beats 90%
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        r, c = len(grid), len(grid[0])
        def isValid(nr, nc):
            if 0 <= nr < r and 0 <= nc < c: return True
            else: return False
        
        def helper():
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1: yield((i, j))
        
        res = 0
        queue = deque()
        for ri, cj in helper():
            queue.append((ri, cj))
            grid[ri][cj] = 2
            count = 1
            while queue:
                ri, cj = queue.pop()
                for i, j in directions:
                    nr, nc = ri + i, cj + j
                    if isValid(nr, nc) and grid[nr][nc] == 1:
                        count += 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            res = max(res, count)
        return res


#class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         seen = set()
#         def area(r, c):
#             if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
#                     and (r, c) not in seen and grid[r][c]):
#                 return 0
#             seen.add((r, c))
#             return (1 + area(r+1, c) + area(r-1, c) +
#                     area(r, c-1) + area(r, c+1))

#         return max(area(r, c)
#                    for r in range(len(grid))
#                    for c in range(len(grid[0])))
        