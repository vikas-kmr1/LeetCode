class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         size = len(nums)
#         hash_map = Counter(nums)
        
#         return max(hash_map.keys(), key = hash_map.get )
