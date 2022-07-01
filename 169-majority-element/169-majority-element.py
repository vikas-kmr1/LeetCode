class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        while(len(nums)):
            n = nums[0]
            s  = nums.count(n)
            
            if s >= len(nums)/2:
                return n
            else:
                for i in range(s):
                    nums.remove(n)
                    
        