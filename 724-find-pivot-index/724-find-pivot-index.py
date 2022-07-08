class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_sum = 0
        
        for i in range(n):

            if left_sum == sum(nums[i+1:]):
                return i
            else:
                left_sum += nums[i]
                
        return -1
        