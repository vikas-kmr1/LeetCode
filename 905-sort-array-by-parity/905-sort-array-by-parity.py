class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            if i%2 == 0:
                lst.insert(0,i)
            else:
                lst.append(i)
        return lst
            
        
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 val = nums[i]
#                 nums.pop(i)
#                 nums.insert(0,val)
                
                
#         return nums


                
                
        