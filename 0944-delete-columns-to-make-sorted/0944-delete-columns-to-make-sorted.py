class Solution:

#     #O(NM)
      def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))