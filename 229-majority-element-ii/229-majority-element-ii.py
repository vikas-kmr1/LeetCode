class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashT = Counter(nums)
        
        result = []
        
        for i in set(nums):
            if hashT.get(i) > len(nums)//3:
                result.append(i)
                
        return result
            
            