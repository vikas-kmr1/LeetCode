class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        hash_map = Counter(nums)
        
        return max(hash_map.keys(), key = hash_map.get )
        
#         while(len(nums)):
#             n = nums[0]
#             s  = nums.count(n)
            
#             if s >= len(nums)/2:
#                 return n
#             else:
#                 for i in range(s):
#                     nums.remove(n)
                    
        