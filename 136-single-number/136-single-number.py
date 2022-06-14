class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_ = set(nums)
        for i in set_:
            if(nums.count(i) == 1):
                return i
        