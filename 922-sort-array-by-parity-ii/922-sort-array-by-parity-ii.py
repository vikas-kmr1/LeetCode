class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_pointer = 0
        odd_pointer = 1
        lst = [None]*len(nums)
        
        for i in range(len(nums)):
            if nums[i]%2 == 0 :
                lst[even_pointer] = nums[i] 
                even_pointer+=2
                
            else:
                lst[odd_pointer] =  nums[i] 
                odd_pointer+=2
        return lst
            
        
        