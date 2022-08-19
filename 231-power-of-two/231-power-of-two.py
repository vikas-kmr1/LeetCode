class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = format(n,"b")
        if n == 2**(len(s)-1):
            return True
        return False
        