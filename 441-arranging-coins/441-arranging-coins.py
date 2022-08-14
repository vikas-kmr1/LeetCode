class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high = 1, n
        ans  = 0
        
        while n > 0:
            if n < low:
                break
            else:    
                n -= low
                low+=1
            
        return low-1
            
      