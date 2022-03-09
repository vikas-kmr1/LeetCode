class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count_ele = 0 
        max = count_ele
        
        for i in nums:
            if i == 1:
                count_ele += 1
            else:
                count_ele = 0
                
            if max <= count_ele:
                max = count_ele
        return max
                
        