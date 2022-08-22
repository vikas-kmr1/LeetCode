class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) >= 3:
            return nums[-3]
        return nums[-1]
        
        
#         f_max,s_max,t_max = 0,0,-1*(2**31-1)
        
#         for i in nums:
#             if i > f_max:
#                 s_max = f_max
#                 f_max = i
                
#             elif i > s_max and i < f_max :
#                 t_max = s_max
#                 s_max = i
#             elif i > t_max and i < s_max:
#                 t_max = i
        
#         if t_max <= -1*(2**31-1) :
#             return f_max
#         return t_max

                
        