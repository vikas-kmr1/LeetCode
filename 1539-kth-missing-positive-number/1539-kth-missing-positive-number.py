class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ptr, number = 0,0
        while k != 0:
            number += 1
            if ptr < len(arr) and arr[ptr] == number:
                ptr += 1
                continue
            k -= 1
        return number