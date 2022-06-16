class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        i=0
        while(i<len(nums)):
            if nums[i] in dup:
                nums.pop(i)
            else:
                dup.append(nums[i])
                i+=1
        return i
            
        