class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high = 0, n-1
        
        if n ==1:
            return 1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if n == mid*(mid+1)//2:
                return mid
            elif n > mid*(mid+1)//2:
                low  = mid + 1
                ans = mid
            else:
                high = mid - 1
                
        return ans
            
        
        
        #brute force T.C = O(n)
#         while n > 0:
#             if n < low:
#                 break
#             else:    
#                 n -= low
#                 low+=1
            
#         return low-1
            
      