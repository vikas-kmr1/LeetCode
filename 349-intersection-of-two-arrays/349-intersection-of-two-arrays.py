class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)
    
        result = []
    
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1 
        
        for i in nums1:
            if i in nums2:
                result.append(i)
        return result
        
        
    

    # return set(nums1).intersection(set(nums2))
        