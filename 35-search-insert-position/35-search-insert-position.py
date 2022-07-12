
                

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
              return self.search(nums, 0, len(nums)-1, target)      

    def search(self, a, s, e, val):
        if s>e:
            return s
        else:
            if val==a[(s+e)//2]:
                return (s+e)//2
            elif val>a[(s+e)//2]:
                return self.search(a, (s+e)//2+1, e, val)
            else:
                return self.search(a, s, (s+e)//2-1, val)
        
        
        
        
        
        
        # iterative approach
#         start , end =  0 , len(nums)-1

#         while start <= end:
#             mid  = (start+end)//2
            
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 start = mid+1
#             else:
#                 end = mid-1 
                
#         return start     
        
        
        
        
        
        