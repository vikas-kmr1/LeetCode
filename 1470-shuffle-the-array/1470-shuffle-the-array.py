class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        
        for x,y in zip(nums[0:n],nums[n:]):
            ans.extend([x,y])
        return ans