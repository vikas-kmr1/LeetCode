class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        m = len(set(candyType))
        if m <= n:
            return m
        return n
        
        