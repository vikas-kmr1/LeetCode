# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
        
#         n = len(nums)
        
#         total = (n*(n+1))//2
        
#         return(total - sum(nums))
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res