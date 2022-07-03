class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                val = nums[i]
                nums.pop(i)
                nums.insert(0,val)
                
                
        return nums
                
                
        