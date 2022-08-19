class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        arr_temp = nums[:]
        nums.sort()
        val_table = {nums[0]:0}
    
        for i,n in enumerate(nums):
            if n not in val_table:
                val_table[n] = i
            
        return [val_table[n] for n in arr_temp]
        
        
                       
                      
            
            
        
        
        
        
        #brute force
#         ans = [None]*len(nums)
        
#         for i in range(len(nums)):
#             cnt = 0
#             for j in nums:
#                 if j < nums[i]:
#                     cnt += 1
                
#             ans[i] = cnt
#         return ans
                
        