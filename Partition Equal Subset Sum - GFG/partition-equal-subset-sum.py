# User function Template for Python3

class Solution:
    def equalPartition(self, N, nums):
        # Calculate the total sum of the numbers in the array
        total_sum = sum(nums)
        
        # Check if the total sum is odd, in which case it's impossible to partition
        if total_sum % 2:
            return False
        
        # Calculate the target sum for each partition
        target_sum = total_sum // 2
        
        # Initialize a dynamic programming table to track if a sum is achievable
        # dp[i] will be True if a sum of i is achievable, otherwise False
        dp = [1 if i == 0 else 0 for i in range(target_sum + 1)]
        
        for num in nums:
            # Create a set to track the achieved sums for the current number
            achieved_sums = set()
            
            # Iterate through the dp table from 'num' to 'target_sum'
            for j in range(num, target_sum + 1):
                # Check if we can achieve sum 'j' by including or excluding the current number 'num'
                if dp[j] == 0 and dp[j - num] and (j - num) not in achieved_sums:
                    dp[j] = 1
                    achieved_sums.add(j)
                # If the target sum is achieved, return True
                if dp[target_sum]:
                    return 1
        
        # If no partition is found, return False
        return 0
            
            
            
        
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends