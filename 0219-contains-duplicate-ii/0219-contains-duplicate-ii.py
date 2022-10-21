class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        else:
            
            d = dict()
            for i in range(len(nums)):
                if nums[i] in d and abs(i - d[nums[i]]) <= k:
                    return True
                d[nums[i]] = i
            return False
                
                    
         