class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            ans = []
            for j in range(n):
                left = set()
                r = i - 1
                l = j -1
                while r >= 0 and l >= 0:
                    left.add(grid[r][l])
                    r -= 1
                    l -= 1
                
                right = set() 
                r = i + 1
                l = j + 1
                while r < m and l < n:
                    right.add(grid[r][l])
                    r += 1
                    l += 1
            
                ans.append( abs(len(right)- len(left)) )
            res.append(ans)
        return res
                    
                    
                
        