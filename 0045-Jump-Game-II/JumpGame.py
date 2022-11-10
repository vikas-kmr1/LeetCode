#T.C: O(n) where n is the length of the list
#S.C: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps  = 0
        currStep, maxSteps = 0 , 0

        ind = 0
        while currStep < len(nums)-1:
           
            maxSteps = max(maxSteps ,ind + nums[ind])
           
            if  ind == currStep:
                jumps += 1
                currStep = maxSteps
           
            ind += 1

        return jumps
