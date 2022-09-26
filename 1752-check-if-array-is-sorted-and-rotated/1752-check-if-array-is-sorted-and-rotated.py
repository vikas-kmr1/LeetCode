class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        
        cnt = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                cnt += 1
            
        
        if nums[-1] > nums[0]:
            cnt += 1
            
        
        return cnt <= 1
                
        
        