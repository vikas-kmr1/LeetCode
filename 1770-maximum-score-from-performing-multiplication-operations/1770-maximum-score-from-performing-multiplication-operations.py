class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        m = len(multipliers)
        n = len(nums)

        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards

            for left in range(op, -1, -1):

                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])

        return dp[0]


# class Solution:
#     def maximumScore(self, nums, multipliers):

#         # Number of Operations
#         m = len(multipliers)

#         def helper(nums, op):
#             if op == m:
#                 return 0

#             return max(nums[0] * multipliers[op] + helper(nums[1:], op+1),
#                        nums[-1] * multipliers[op] + helper(nums[:-1], op+1))

#         return helper(nums, 0)