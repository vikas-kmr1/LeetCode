class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.countOnes(i) for i in range(n+1) ]
        
    def countOnes(self,n):
        cnt = 0
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt
        