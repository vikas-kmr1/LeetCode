class Solution:
    def rotate(self, nums: List[int], k: int) :
        l = len(nums)
        k = k % l
        nums[:] = nums[(l-k):] + nums[:(l-k)]


#         for i in range(k):
#             for j in range(len(nums)-1,0,-1):
#                 nums[j],nums[j-1]  = nums[j-1],nums[j]
            
    
        
        
       