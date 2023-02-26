class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        lSum ,rSum = 0,sum(nums)
        
        for i,n in enumerate(nums):
            rSum -= n
            ans.append( abs(lSum - rSum))
            lSum += n
        return ans
                