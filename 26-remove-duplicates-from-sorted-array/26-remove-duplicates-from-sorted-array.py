class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==0 : return 0
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1

        
        
        
        
        
        #brute force
#         dup = sorted(set(nums))
#         i = 0
#         for x in dup:
#             nums[i] = x
#             i+=1
       
#         while(i<len(nums)):
#             nums[i] = None
#             i+=1
            
     
#         return len(dup)
            
        