# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        
        
        totalSum = sum(A)
        currSum = 0
        for i in range(N):
            currSum += A[i]
            
            if currSum == totalSum:
                return i + 1
            totalSum -= A[i]
            
            
        return  -1
            
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends