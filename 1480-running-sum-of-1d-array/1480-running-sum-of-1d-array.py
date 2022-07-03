class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        lst = []
        for i in range(len(nums)):
            s+=nums[i]
            lst.append( s)
            
        return lst
#         sum_ = 0
#         for i in range(len(nums)):
#             sum_ += nums[i]
#             nums[i] = sum_
            
#         return nums
        
        
        