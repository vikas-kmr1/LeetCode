class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return ((n-1)*4) + self.coloredCells(n-1)
        
        
            
        