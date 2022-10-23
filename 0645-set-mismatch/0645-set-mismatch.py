class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        missing_number = abs(sum(set(nums)) -  (len(nums)*(len(nums)+1) // 2))
                                       
        distinct_key = {}
        for n in nums:
            if n in distinct_key:
               return [n,missing_number]
            
            distinct_key[n] = 1
                                       
                                     
                
        