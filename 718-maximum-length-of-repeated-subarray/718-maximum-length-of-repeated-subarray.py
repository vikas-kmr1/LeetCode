class Solution(object):
    def findLength(self, A, B):
        cache = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    cache[i][j] = cache[i + 1][j + 1] + 1
        return max(max(row) for row in cache)