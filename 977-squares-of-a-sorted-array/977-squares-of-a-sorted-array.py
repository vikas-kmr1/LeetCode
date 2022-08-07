class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        
        l_index =  0
        r_index = len(nums) - 1
        
        i = len(nums)-1
        while i >= 0:
            left_val = abs(nums[l_index])
            right_val = abs(nums[r_index])
            
            if left_val >= right_val:
                ans[i] = left_val ** 2
                l_index += 1
            else:
                ans[i] = right_val ** 2
                r_index -= 1
        
            i -= 1
        return ans
                
            
        
    
    
    
    
#    using inbuild methods    
#         squares=[ i**2 for i in nums] 
#         squares.sort()
#         return squares
        