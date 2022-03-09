class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            if len(str(i)) % 2 == 0 :
                counter += 1
                
        return counter
        