class Solution:
   def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp1, dp2 = [0]*(target + 1), [0]*(target + 1)
        ub = min(target, k)
        for j in range(1, ub + 1):
            dp1[j] = 1
        for i in range(1, n):
            s = 0
            for j in range(1, target + 1):
                s += dp1[j - 1]
                dp2[j] = s%(10**9 + 7)
                if j > k:
                    s -= dp1[j - k]
                if j > i and not s:
                    break
            dp1 = dp2[:]
        return dp1[-1]