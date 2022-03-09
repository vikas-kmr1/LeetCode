def fun(nums1,nums2):
        lst=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                lst.append(i)
        return lst

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return fun(nums2,nums1)
        else:
            return fun(nums1,nums2)
        
    
    
        
        