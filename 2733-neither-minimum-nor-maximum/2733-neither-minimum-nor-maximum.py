class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # n, m = min(nums), max(nums)
        # for num in nums:
        #     if n != num != m:
        #         return num
        # return -1
        
        return sorted(nums[:3])[1] if len(nums) > 2 else -1