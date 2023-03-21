class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for n in nums:
            if n:
                ans += (cnt * (cnt+1))//2
                cnt = 0
            else:
                cnt += 1
        if cnt:
            ans += (cnt * (cnt+1))//2
        return ans
            
        