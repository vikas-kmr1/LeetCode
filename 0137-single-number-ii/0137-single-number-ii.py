class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        for n in nums:
            if freq[n] == 1:
                return n