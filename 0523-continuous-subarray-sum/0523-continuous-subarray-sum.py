# Time complexity: O(nums.length).

# We perform O(nums.length) operations with a hash map, each taking O(1) time on average.

# Space complexity: O(min {nums.length, k}).

# The size of a hash map does not exceed nums.length+1. It also does not exceed k because there are only k possible remainders.


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder_map = {0 : 0}
        s = 0
        for i,n in enumerate(nums):
            
            s += n
            
            if s%k not in remainder_map:
                remainder_map[s % k] = i + 1
                
            elif remainder_map[s % k] < i:
                return True
            
        return False
                
                
        
        
        