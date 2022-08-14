class Solution:
    def searchRange(self, nums: List[int], target: int):
        
        try:
            first=nums.index(target)
            num1=nums[::-1]
            last=len(nums)-(num1.index(target))-1
            return [first,last]
        
        except ValueError:
            return [-1,-1]
            
       