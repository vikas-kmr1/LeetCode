class Solution:
    def search(self, nums: List[int], target: int) :
        try:
            return nums.index(target)
        except:
            return -1
        