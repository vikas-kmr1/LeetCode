class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0 
        l = len(arr)-1
        while i <= l :
            
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop(len(arr) -1)
                i += 1
                
            i += 1
            
        