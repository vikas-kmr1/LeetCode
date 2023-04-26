#T.C: O(n)
#S.C: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            if n - 1  not in hashset:
                streak = 1
                while n + streak in hashset:
                    streak += 1
                longest = max(longest,streak)
        return longest
                
            
            
            
            