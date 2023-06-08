class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
        
#         cnt = 0
#         n,m = len(grid), len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] < 0:
#                     cnt += (n - i) * (m-j) 
#                     m = j
#                     break
#             if m == 0:
#                 break
#         return cnt
                
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = m - 1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n - c
                r -= 1
            else:
                c += 1
        return cnt
        