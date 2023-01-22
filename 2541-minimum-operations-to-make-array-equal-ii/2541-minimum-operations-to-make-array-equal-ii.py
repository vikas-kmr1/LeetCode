class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if not k:
            return 0 if nums1 == nums2 else -1
        ops = bal = 0
        for x , y in zip(nums1,nums2):
            rem = x - y
            
            if rem % k:
                return -1
            
            bal += rem
            if x > y:
                ops += rem // k

        return ops if not bal else -1
        
    
