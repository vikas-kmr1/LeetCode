
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         # Calculate the total sum of the numbers in the array
#         total_sum = sum(nums)
        
#         # Check if the total sum is odd, in which case it's impossible to partition
#         if total_sum % 2:
#             return False
        
#         # Calculate the target sum for each partition
#         target_sum = total_sum // 2
        
#         # Initialize a dynamic programming table to track if a sum is achievable
#         # dp[i] will be True if a sum of i is achievable, otherwise False
#         dp = [1 if i == 0 else 0 for i in range(target_sum + 1)]
        
#         for num in nums:
#             # Create a set to track the achieved sums for the current number
#             achieved_sums = set()
            
#             # Iterate through the dp table from 'num' to 'target_sum'
#             for j in range(num, target_sum + 1):
#                 # Check if we can achieve sum 'j' by including or excluding the current number 'num'
#                 if dp[j] == 0 and dp[j - num] and (j - num) not in achieved_sums:
#                     dp[j] = 1
#                     achieved_sums.add(j)
#                 # If the target sum is achieved, return True
#                 if dp[target_sum]:
#                     return 1
        
#         # If no partition is found, return False
#         return 0
        
        
        # O(2^len(nums))        
#         if sum(nums)&1:return False
        
#         target = sum(nums)//2
        
#         def dfs(curr,i):
#             if   i < 0 or i  >= len(nums) or curr > target:
#                 return False
#             if curr == target:return True
#             return dfs(curr,i+1) or dfs(curr+nums[i], i+1)
        
#         return dfs(0,0)
            
            
            
        