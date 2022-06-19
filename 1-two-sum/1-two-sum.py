class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val_map = {}
        for i in range(len(nums)) :
            if (target - nums[i]) in val_map: 
                return [val_map[target - nums[i]],i]
            else :
                val_map[nums[i]] = i
        
    
#         for i in range(len(nums)-1):
#             l=target - nums[i]
#             try:
#                 if l in nums:
#                     return [i,i+1+(nums[i+1:].index(l))]
#             except:
#                 continue
        
            
            
            
            
            
            