class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # leftSum represents the sum of the first i + 1 elements at index i
        n, totalSum, leftSum = len(nums), sum(nums), 0
        
        # res[0] is the minimum absolute difference, and res[1] is the index.
        res = [inf,inf]
        
        for i,v in enumerate(nums):
            leftSum += v
            
            leftAvg = leftSum//(i+1)
            # when we are at the last index, the right hand side sum is 0. (To aviod divide by zero error)
            rightAvg = (totalSum-leftSum)//(n-i-1) if n-i-1!=0 else 0
            absDif = abs(leftAvg-rightAvg)
            
            # min will take care of "If there are multiple such indices, return the smallest one."
            res = min(res,[absDif,i])
        
        # return the index
        return res[1]