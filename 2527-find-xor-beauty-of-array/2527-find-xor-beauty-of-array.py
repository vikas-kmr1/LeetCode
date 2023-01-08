from functools import reduce
from operator import xor
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor,nums)