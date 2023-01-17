class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0
        numSum = 0
        
        for n in nums:
            numSum += n
            
            while n > 0:
                digitSum += (n%10)
                n = n // 10
        return abs(digitSum - numSum)