class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst = []
        for i in arr2:
            lst.extend([i]*arr1.count(i))
            for j in range(arr1.count(i)):
                arr1.remove(i)
        arr1.sort()
        return lst+arr1
            
            
