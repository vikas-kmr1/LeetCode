class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        
        for i in set(nums):
            if hash_map.get(i) >1:
                return i
            
        
        
        
        
        