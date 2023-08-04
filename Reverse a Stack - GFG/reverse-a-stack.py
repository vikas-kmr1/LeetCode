#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        
        start = 0 
        end = len(St) - 1
        
        while start < end:
            St[start], St[end] = St[end], St[start]
            start += 1
            end -= 1
        
        
        return St


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends