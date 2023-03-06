class Solution:
    #def countWays(self, ranges: List[List[int]]) -> int:
    def countWays(self, A: List[List[int]]) -> int:
        pre = -1
        res = 0
        for a,b in sorted(A):
            res += pre < a
            pre = max(pre, b)
        return pow(2, res, 10**9+7)
#         ranges.sort()
#         print(ranges)
#         Olap = []
#         Olap.append(ranges[0])
#         n = len(ranges)
#         cnt = 0
#         if n == 1:
#             return 2
#         for i in range(1,n):
#             if  ranges[i][0] <= Olap[-1][1]:
#                 cnt += 1
#                 Olap[-1][0] = min(ranges[i][0],Olap[-1][0] )
#                 Olap[-1][1] = max(ranges[i][1],Olap[-1][1] )
                
#             else:
#                 Olap.append(ranges[i][:]) 
      
#         return 2 if cnt == n-1 else 2**(n-cnt)%(10**9 + 7)
            