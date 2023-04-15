class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        heap = [-nums[0]]
        result = []
        runningSum = 0
        for num in nums:
            maxSum = max(num, -1 * heapq.heappop(heap))
            result.append(runningSum + num + maxSum)
            runningSum += maxSum+num
            heappush(heap,- maxSum)
        return result
        
        
        