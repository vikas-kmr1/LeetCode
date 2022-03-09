class Solution:
    def peakIndexInMountainArray(self, arr: List[int]):
        start=0
        end=len(arr)-1
        while start<end:
            mid=int(start + (end-start)/2)
            if arr[mid]>arr[mid+1]:
                end=mid
            else:
                start=mid+1
        return start
    
    
        
        
        
        
        
 
       
        
        