class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(num) for num in nums]
        score = 0
        
        for i in range(len(nums[0])):
            n = 0
            for j in range(len(nums)):
                n = max(nums[j].pop(),n)
            score += n
        return score
        
        