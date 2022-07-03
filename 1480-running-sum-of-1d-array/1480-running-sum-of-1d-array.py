class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            nums[i] = sum_
            
        return nums
        
        
        