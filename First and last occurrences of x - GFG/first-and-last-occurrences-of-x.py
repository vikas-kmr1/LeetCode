#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        s,e = self.binarySearch(arr,True,x), self.binarySearch(arr,False,x)    
        return [s,e]
        # code here
    
    def binarySearch(self,arr,isFirst,k):
        start, end  = 0, len(arr) - 1 
        lastFound = -1
        while start <= end:
            mid = start + (end - start) // 2
            if  arr[mid]  >  k:
                end = mid - 1
            elif arr[mid] < k:
                start = mid + 1
            else:
                lastFound = mid
                
                if isFirst:
                    end = mid - 1
                else:
                    start = mid + 1
            
        return lastFound
    
    
    

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends