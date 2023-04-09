from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sum_l = {}
        sum_r = {}
        cnt_l = {}
        cnt_r = {}
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = cnt_l.get(nums[i], 0) * i - sum_l.get(nums[i], 0)
            sum_l[nums[i]] = sum_l.get(nums[i], 0) + i
            cnt_l[nums[i]] = cnt_l.get(nums[i], 0) + 1 
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] += sum_r.get(nums[i], 0) - cnt_r.get(nums[i], 0) * i
            sum_r[nums[i]] = sum_r.get(nums[i], 0) + i
            cnt_r[nums[i]] = cnt_r.get(nums[i], 0) + 1 
        return res
