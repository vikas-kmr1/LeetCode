class Solution:
    def peakIndexInMountainArray(self, A: List[int]):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

    
    
        
        
        
        
        # Iterative approach
        # start=0
        # end=len(arr)-1
        # while start<end:
        #     mid=int(start + (end-start)/2)
        #     if arr[mid]>arr[mid+1]:
        #         end=mid
        #     else:
        #         start=mid+1
        # return start
    
    
        
        
        
        
        

        
        