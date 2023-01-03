class Solution:

    #O(NlogNM), with N <= 100

    def minDeletionSize(self, A):
        return sum(list(col) != sorted(col) for col in zip(*A))