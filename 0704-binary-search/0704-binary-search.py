

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # recusrive 
        def binarySrch(nums,target,left,right):
            if left > right:
                return -1
            pivot = left+(right -left)//2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                return binarySrch(nums,target,left,pivot-1)
            else:
                return binarySrch(nums,target,pivot+1,right)
            
            
        
        
        return binarySrch(nums,target,0,len(nums)-1)
        
        
        
        # iterative method
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     pivot = left + (right - left) // 2
        #     if nums[pivot] == target:
        #         return pivot
        #     if target < nums[pivot]:
        #         right = pivot - 1
        #     else:
        #         left = pivot + 1
        # return -1