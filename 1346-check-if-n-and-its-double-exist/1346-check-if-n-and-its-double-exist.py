class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def binarySearch(nums,target)->bool:
            low = 0 
            high = len(nums) -1
            
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        
        
        arr.sort()
        
        for i in range(len(arr) - 1):
            if arr[i] >= 0:
                
                if binarySearch(arr[i+1:], arr[i]*2):
                    return True
            else:
                if binarySearch(arr[:i], arr[i]*2):
                    return True
            
        return False
                
            
                
        
      