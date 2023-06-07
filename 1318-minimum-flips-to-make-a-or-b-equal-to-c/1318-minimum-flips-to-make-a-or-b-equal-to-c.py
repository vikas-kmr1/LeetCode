class Solution:
    def minFlips(self,a, b, c):
        def popcount(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        return popcount((a | b) ^ c) + popcount(a & b & ((a | b) ^ c))