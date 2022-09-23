# def partition(array, low, high):

#   # choose the last element as pivot
#   pivot = array[high]

#   # pointer for greater element
#   i = low - 1

#   # compare each element with pivot
#   for j in range(low, high):
#     if array[j] < pivot:
#       # if element smaller than pivot is found
#       # swap it with the greater element pointed by i
#       i = i + 1

#       # swapping element at i with element at j
#       (array[i], array[j]) = (array[j], array[i])

#   # swap the pivot element with the greater element specified by i
#   (array[i + 1], array[high]) = (array[high], array[i + 1])

#   # return the position from where partition is done
#   return i + 1

# # function to perform quicksort
# def quickSort(array, low, high):
#   if low < high:

#     pi = partition(array, low, high)

#     quickSort(array, low, pi - 1)

#     quickSort(array, pi + 1, high)




class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0 
        high = len(arr)-1
        
        while mid <= high:
            if arr[mid] == 0:
                (arr[low],arr[mid]) = (arr[mid],arr[low])
                low += 1
                mid += 1
        
            elif arr[mid] == 1:
                mid+=1
            
            elif arr[mid] == 2:
                arr[high],arr[mid] = arr[mid],arr[high]
                high -= 1
        
                
         
#T.C : O(nlogn)
#         quickSort(nums,0, len(nums) - 1)
        
                
                
            
            
        
        