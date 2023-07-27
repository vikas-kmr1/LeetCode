class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n = len(nums)

        return Counter(nums) == Counter(range(1,n)) + Counter((n-1,))
    
                
                
        