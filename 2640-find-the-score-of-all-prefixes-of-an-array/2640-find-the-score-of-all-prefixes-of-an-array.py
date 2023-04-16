#Using min-heap
# class Solution:
#     def findPrefixScore(self, nums: List[int]) -> List[int]:
#         heap = [-nums[0]]
#         result = []
#         runningSum = 0
#         for num in nums:
#             maxSum = max(num, -1 * heapq.heappop(heap))
#             result.append(runningSum + num + maxSum)
#             runningSum += maxSum+num
#             heappush(heap,- maxSum)
#         return result
        
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prevMax = 0 
        result = []
        runningSum = 0
        for i,num in enumerate(nums):
            prevMax = max(num,prevMax)
            nums[i] = runningSum + num + prevMax
            #result.append(runningSum + num + prevMax)
            runningSum += prevMax + num
        return nums
        
        
        