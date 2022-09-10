class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         slow , fast = 0 , 0
#         while True :
#             slow = nums[slow]
#             fast= nums[nums[ fast ] ]
#             if slow == fast :
#                 break
                
#         slow2 = 0
#         while True :
#             slow= nums[slow ]
#             slow2 = nums[slow2]
#             if slow == slow2 :
#                 return slow
        
        
        
        hash_map = Counter(nums)
        
        for i in set(nums):
            if hash_map.get(i) >1:
                return i
            
        
        
        
        
        