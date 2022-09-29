#T.C: O(n)
#T.C: O(1)

# class Solution:
#     def productExceptSelf(self, nums):
#         prod, zero_cnt = reduce(lambda a, b: a*(b if b else 1), nums, 1), nums.count(0)
#         if zero_cnt > 1: return [0]*len(nums)
#         for i, c in enumerate(nums):
#             if zero_cnt: nums[i] = 0 if c else prod
#             else: nums[i] = prod // c
#         return nums

#approach 2   
# Note that the final result would be product of array except self because we only update & multiply pre with nums[i] after updating ans[i] and similarly for suf.

# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def productExceptSelf(self, nums):
        ans ,suf, pre = [1]*len(nums),1,1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]  # prefix product from one end
            ans[-1-i] *= suf
            suf *= nums[-1-i]   # suffix product from other end
        return ans