class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # insertion sort
#         for i in range(1,len(heights)):
#             k = i
#             for j in range(i-1,-1,-1):
#                 if heights[k] > heights[j]:
                    
#                     heights[k], heights[j] = heights[j], heights[k]
#                     names[k],names[j] = names[j],names[k]
#                     k = j
        
        self.heapSort(heights,names)
        return names[::-1]
    
    def heapSort(self, nums,names):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                names[i], names[largest] = names[largest],names[i]
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            names[i], names[0] = names[0],names[i]
            heapify(nums, i, 0) 
                    
                
                