class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        max_amt = 0
        while start < end:
            min_height = min(height[start],height[end])
            x_distance = end -start
            
            max_amt = max(max_amt,(min_height * x_distance))
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_amt
            
        
        
        