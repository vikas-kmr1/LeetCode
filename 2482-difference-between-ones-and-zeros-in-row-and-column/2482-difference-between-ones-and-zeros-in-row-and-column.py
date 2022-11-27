class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        
        zerosRows = [0 for _ in range(m)]
        zerosCols = [0 for _ in range(n)]
        onesRows  = [0 for _ in range(m)]
        onesCols  = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRows[i] += 1
                    onesCols[j] += 1
                else:
                    zerosRows[i] += 1
                    zerosCols[j] += 1
                    
        for i in range(m):
            for j in range(n):
                grid[i][j] = onesRows[i] + onesCols[j] - zerosRows[i] - zerosCols[j]
        
        return grid