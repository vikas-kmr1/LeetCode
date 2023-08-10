class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        while i < len(nums)-1 and nums[i] <= nums[i+1]:
            i += 1
        
        nums = nums[i+1:] + nums[:i+1]
 
        print(nums)
        start,end = 0 , len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False                 
                
            
        
        