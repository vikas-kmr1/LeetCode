class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        pSum = 0
        for i in range(len(nums)):
            if nums[i] + pSum <= 0:
                return i 
            pSum += nums[i]
        
        return len(nums)
            
        