class Solution:
    def searchRange(self, nums: List[int], target: int):
        
        def binarySearch(firstFound):
            a = -1
            low = 0 
            high = len(nums)-1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    a = mid
                    if firstFound:
                        low = mid+1
                        
                    else:
                        high = mid - 1
                        
                elif nums[mid] > target:
                    high  = mid -1
                else:
                    low  = mid +1
            return a
                
            
        
        
        ans = [-1,-1]
        ans[0] = binarySearch(False)
        
        ans[1] = binarySearch(True)
        
        return ans
    
    
    # beginner's solution
#         try:
#             first=nums.index(target)
#             num1=nums[::-1]
#             last=len(nums)-(num1.index(target))-1
#             return [first,last]
        
#         except ValueError:
#             return [-1,-1]
            
       