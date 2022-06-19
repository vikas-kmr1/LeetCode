class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        for i in range(len(nums)-1):
            l=target - nums[i]
            try:
                if l in nums:
                    return [i,i+1+(nums[i+1:].index(l))]
            except:
                continue
        
            
            
            
            
            
            