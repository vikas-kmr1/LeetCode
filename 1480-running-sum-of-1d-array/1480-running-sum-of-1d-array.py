class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if i == 0:
                nums[i]+=0
            else:
                nums[i] += nums[i-1]     
        return nums
        
        # s = 0
        # lst = []
        # for i in range(len(nums)):
        #     s+=nums[i]
        #     lst.append( s)
            
        #return lst

        
        