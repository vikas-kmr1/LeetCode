class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        lst_odd = []
        lst_even = []
        
        for i in range(len(nums)):
            if i%2 == 0:
                lst_even.append(nums[i])
            else:
                lst_odd.append(nums[i])
                
        
        lst_odd.sort()
        lst_odd.reverse()
        lst_even.sort()

        
        ans =[]
        
        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(lst_even[0])
                lst_even.pop(0)
            else:
                ans.append(lst_odd[0])
                lst_odd.pop(0)
        
        return ans