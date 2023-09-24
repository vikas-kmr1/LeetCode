from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	freq = Counter(arr)
    	a = list()
    	for k,v in freq.items():
    	    if v > 1:
    	        a.append(k)
    	        
    	return sorted(a) if len(a) > 0 else [-1] 
    	    

                    
        
    	
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends