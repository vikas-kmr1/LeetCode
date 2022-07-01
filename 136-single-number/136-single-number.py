class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while(len(nums)>0):
            j = nums[0]
            s = nums.count(j)
            
            if s == 1:
                return j
            else:
                
                for i in range(s):
                    nums.remove(j)
            
        