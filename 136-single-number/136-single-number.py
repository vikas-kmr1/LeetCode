class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)
        
#         ans=[]
#         for i in nums:
#             if i not in ans:
#                 ans.append(i)
#             else:
#                 ans.remove(i)
                    
#         return ans[0]
    
    
