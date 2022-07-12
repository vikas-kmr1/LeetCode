class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if (high%2 == 0 and low%2 == 0):
            return ((high-low)//2)
        
        else:
            return ((high-low)//2) +1
            
        