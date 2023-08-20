#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
        left , right = 0 , n-1
        
        while left <= right:
            if arr[left] < x:
                left += 1
            
            if arr[right] > x:
                right -= 1
            
            if arr[right] == x == arr[left]:
                return right -left + 1
        return 0
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends