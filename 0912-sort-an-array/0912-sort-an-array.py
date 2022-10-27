class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        
        self.heapSort(arr)
        return arr
        
        
    def heapSort(self, nums):
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
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 