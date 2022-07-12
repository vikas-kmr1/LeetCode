class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumMx=sum(nums)
        curr=0
        
        if len(nums)==1:
                return nums[0]
            
        for i in nums:
            curr+=i
            if curr>sumMx:
                sumMx=curr
                print(sumMx)
            if curr<0:
                curr=0
            
                
        return sumMx 