class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        
        below = triangle[-1]
        
        for row in range(n-2, -1, -1):
            curr = [-1] * (row + 1)
            for col in range(row + 1):
                smallestOption = min(below[col], below[col + 1])
                curr[col] = triangle[row][col] + smallestOption
            below = curr
        
        return below[0]