# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n
        
        while(s<=e):

            if guess((s+e)//2) == -1:
                e = (s+e)//2 - 1
            elif guess((s+e)//2) == 1:
                s = (s+e)//2 + 1
            elif guess((s+e)//2) == 0:
                return (s+e)//2
        
        