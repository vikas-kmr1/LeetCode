class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        if not nums or len(nums) <= 1:
            return
        
        def swap(i,j):
            nums[i], nums[j] = nums[j],nums[i]
            
        def reverseNums(i,j):
            while i < j:
                swap(i,j)
                i += 1 
                j -= 1
        
        ind =  len(nums)-2
        
        while ind >=0 and nums[ind] >= nums[ind + 1]:
            ind -= 1
        
        
        
            
        if ind >= 0:
            ind2 = len(nums) -1
            
            while nums[ind2] <= nums[ind]:
                ind2 -= 1
            
            #swap the elelemets at ind and ind2
            swap(ind,ind2)
            
        reverseNums(ind+1,len(nums) - 1)
            
            
                
                
            
            
            
            
        
        
        
        
        
         