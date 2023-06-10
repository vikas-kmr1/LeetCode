class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)
        
        s = s + str(2*n) + str(3*n)
    
        ans = set(s)

        return len(ans) == 9 == len(s) and '0' not in ans
        
        