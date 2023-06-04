class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        minNumI, maxNumI  = nums.index(1) , nums.index(n)
        
        ans = minNumI + n - maxNumI - 1
     
        return ans if minNumI < maxNumI else ans - 1
        
        
        
    
        