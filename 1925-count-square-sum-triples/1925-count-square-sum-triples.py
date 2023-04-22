class Solution:
    def countTriples(self, n: int) -> int:
        freq = { i**2 :i for i in range(1,n+1)}
        cnt= 0
        for a in range(1,n+1):
            b = 1
            while a**2 + b**2 <= n**2 and b <= n:
                if (a**2 + b**2) in freq:
                    cnt += 1
                b += 1
        return cnt
                
        