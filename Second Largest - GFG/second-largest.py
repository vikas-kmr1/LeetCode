#User function Template for python3
import sys
class Solution:

	def print2largest(self,arr, n):
	    
	    if n<2:
	        return -1
	        
	    s , l = -1, -1
	    
	    for i in range(n):
	        if arr[i] > l:
	            s = l
	            l = arr[i]
	        
	        elif arr[i] > s and arr[i] != l:
	            s = arr[i]
	             
	        
	        
		# code here
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends