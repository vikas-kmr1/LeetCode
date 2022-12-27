# # T.C: O( n.log(n) )
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         return [self.countOnes(i) for i in range(n+1) ]
        
#     def countOnes(self,n):
#         cnt = 0
#         while n:
#             n = n & (n-1)
#             cnt += 1
#         return cnt
        
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp