#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        s,e = self.binarySearch(False,arr,x), self.binarySearch(True,arr,x)    
        return [s,e]
        # code here
    
    def binarySearch(self,firstFound,nums,target) -> int:
        a = -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                a = mid
                
                if firstFound:
                    low = mid + 1
                
                else:
                    high = mid - 1
                
            
            elif nums[mid] > target:
                high = mid -1
            
            else:
                low = mid + 1
        
        return a
        
    
    
    

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