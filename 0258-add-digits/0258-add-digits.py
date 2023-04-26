class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            n = num
            newNum = 0
            while n:
                newNum += n%10
                n = n//10
                
            num = newNum
        return num
                
                