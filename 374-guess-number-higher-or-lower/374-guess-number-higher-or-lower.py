# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while(start<=end):
            mid = start + (end - start)//2
            print(mid)
            if guess(mid) == -1:
                end = mid - 1
            elif guess(mid) == 1:
                start = mid + 1
            elif guess(mid) == 0:
                return mid
        
        