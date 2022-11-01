class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        s = 0 
        cnt = 0
        for n in nums:
            if n%2:
                continue
            
            if n%3 == 0:
                s += n
                cnt += 1
        
        return s//cnt if s else 0
        
        