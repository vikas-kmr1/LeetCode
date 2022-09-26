class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0 
        cnt = 0
        for i in nums:
            if i == 0:
                cnt = 0
            else:
                cnt += 1
            max_cnt = max(cnt,max_cnt)
        
        return max_cnt
            
          
                
        