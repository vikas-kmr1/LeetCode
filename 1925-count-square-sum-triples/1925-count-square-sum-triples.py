class Solution:
    def countTriples(self, n: int) -> int:
        freq = { i**2 :i for i in range(1,n+1)}
        cnt= 0
        for a in range(1,n+1):
            for b in range(1,n+1):
                if (a**2 + b**2) in freq:
                    cnt += 1
        return cnt
                
        