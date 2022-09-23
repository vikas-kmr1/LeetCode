class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #kadane's algo
        #T.C: O(n)
        #S.C: O(1)
        
        current_sum = nums[0]
        max_sum = nums[0]
        
        for n in nums[1:]:
            
            current_sum = max(n, current_sum+n)
            
            max_sum = max(max_sum,current_sum)
            
    
        
        return max_sum
        