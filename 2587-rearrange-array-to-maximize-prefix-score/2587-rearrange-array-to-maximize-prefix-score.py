class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        cnt = 0
        for n in nums:
            if n <= 0:
                return cnt
            cnt += 1
            
        return cnt
            
        