class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int( c**0.5 )
        
        while low <= high:
            if low**2 + high**2  == c:
                return True
            
            elif  low**2 + high**2  > c:
                high -= 1
                
                
            else:
                low += 1
        
            
        return False