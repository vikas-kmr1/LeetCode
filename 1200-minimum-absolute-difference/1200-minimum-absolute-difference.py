class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        difference = {}
        
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff not in difference:
                difference[diff] = [[arr[i - 1], arr[i]]]
            else:
                difference[diff] += [[arr[i - 1], arr[i]]]
        
        return difference[min(difference)]