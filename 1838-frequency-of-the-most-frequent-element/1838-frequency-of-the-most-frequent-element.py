class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if n <= 1: return n
        
        nums.sort()
        Sum, left, right = 0,0,0
        res = 0
        while right < n:
            Sum += nums[right]
            while nums[right] * (right - left + 1) > Sum + k:
                Sum -= nums[left]
                left += 1
            res = max(res,right - left + 1)
            right += 1
                
        return res
            

        