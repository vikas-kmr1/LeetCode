class Solution:
    def minimizeArrayValue(self,A):
        sum = 0
        res = 0;
        for  i in range(len(A)): 
            sum += A[i]
            res = max(res, (sum + i) // (i + 1))

        return res
        