class Solution:
    def triangleNumber(self, A: List[int]) -> int:
        A.sort(); 

        count = 0
        n = len(A)
        for i in range(n - 1, 0, -1):
            l = 0;
            r = i - 1;
            while(l < r):
                if(A[l] + A[r] > A[i]):

                # If it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1]..a[r-1], a[r] and a[i]
                    count += r - l; 

                # checking for more possible solutions
                    r -= 1; 
            
                else:

                # if not possible check for 
                # higher values of arr[l]
                    l += 1; 
        return count

                
            
        