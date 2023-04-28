class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        longest = 1
        l , r = 0,1
        
        while r < len(nums):
            if nums[r] > nums[r - 1]:
                r += 1
            
            else:
                longest = max(longest , r - l )
                l = r
                r += 1
        longest = max(longest , r - l )
        return longest
            
            
        
        