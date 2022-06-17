class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = sorted(set(nums))
        i = 0
        for x in dup:
            nums[i] = x
            i+=1
       
        while(i<len(nums)):
            nums[i] = None
            i+=1
            
     
        return len(dup)
            
        