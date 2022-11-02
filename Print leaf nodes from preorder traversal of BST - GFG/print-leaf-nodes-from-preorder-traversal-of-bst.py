#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		# code here
		ret = []
		def collect(xs):
		    nonlocal ret
		    if len(xs) <= 1:
		        if xs:
		            ret.append(xs[0])
		        return
		    
		    collect([x for x in xs if x < xs[0]])
		    collect([x for x in xs if x > xs[0]])
		    
	    collect(arr)
	    return ret



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends