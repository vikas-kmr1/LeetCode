#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        left, right = 0 , 0
        totalSum = 0
        while right < n  :
            totalSum += arr[right]
            while totalSum > s and left < right:
                totalSum -= arr[left]
                left += 1
            
            if totalSum == s:
                return [left + 1, right + 1]
            right += 1
                
        return [-1]
            
            #Write your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends