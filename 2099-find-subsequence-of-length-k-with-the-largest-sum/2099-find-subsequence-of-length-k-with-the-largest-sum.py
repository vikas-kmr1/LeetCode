class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == k:
            return nums
        
        lst = []
        for i in nums:
            if len(lst) < k:
                lst.append(i)
            else:
                min_val = min(lst)
                if min_val < i:
                    lst.remove(min_val)
                    lst.append(i)
        return lst