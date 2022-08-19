class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        hashmap = {}
        
        for n in nums:
            if hashmap.get(n):
                return True
            if hashmap.get(n) == None:
                hashmap[n]=1
        return False
                

        
                                                    
        # if len(nums)!= len(set(nums)):
        #     return True 
        # return False