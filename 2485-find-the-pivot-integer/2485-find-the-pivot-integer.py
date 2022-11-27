class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        sum_N = (n *(n+1))//2
        
        current_Sum = 0
        for i in range(1,n+1):
            current_Sum += i
            sum_N -= i
            if current_Sum+i+1 == sum_N:
                return i+1
        return -1