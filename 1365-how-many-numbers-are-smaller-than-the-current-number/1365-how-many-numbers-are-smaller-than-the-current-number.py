class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = [None]*len(nums)
        
        for i in range(len(nums)):
            cnt = 0
            for j in nums:
                if j < nums[i]:
                    cnt += 1
                
            ans[i] = cnt
        return ans
                
        