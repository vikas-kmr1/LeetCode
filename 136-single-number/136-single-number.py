class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans=[]
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)
                    
        return ans[0]
    
    
        
#         while(len(nums)>0):
#             j = nums[0]
#             s = nums.count(j)
#             if s == 1:
#                 return j
#             else:
                
#                 for i in range(s):
#                     nums.remove(j)
            
        