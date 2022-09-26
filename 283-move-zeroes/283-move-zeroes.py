class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n :
            if nums[i] != 0:
                i+=1
               
            else:
                nums.append(nums.pop(i)) 
                n -= 1