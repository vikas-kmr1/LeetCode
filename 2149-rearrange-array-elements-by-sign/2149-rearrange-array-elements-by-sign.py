class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)
        i = 0
        
        j = 1
        
        for n in nums:
            if n >= 0:
                ans[i] = n
                i += 2
                
            else:
                ans[j] = n
                j += 2
                
        return ans
            
        