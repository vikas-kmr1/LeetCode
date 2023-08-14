#User function Template for python3

from collections import Counter 
class Solution:
	def singleNumber(self, nums):
		# Code here
		
        freq = Counter(nums)
        
        res = []
        for k,v in freq.items():
            if v == 1:
                res.append(k)
        
        return sorted(res)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends