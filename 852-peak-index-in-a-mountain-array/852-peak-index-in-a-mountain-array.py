class Solution:
    def peakIndexInMountainArray(self, arr: List[int]):
        return arr.index(max(arr))

        #return self.BinaryPeak(arr,0,len(arr)-1)
    
# recursice approach    
#     def BinaryPeak(self,ar, s,e):
        
#         if s>=e:
#             return s
        
#         elif ar[(s+e)//2] > ar[(s+e)//2 + 1]:
#             return self.BinaryPeak(ar,s,(s+e)//2)
#         else:
#             return self.BinaryPeak(ar,(s+e)//2+1,e)
        
    
    
        
        
        
        
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
    
    
        
        
        
        
        

        
        