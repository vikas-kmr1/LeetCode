class Solution:
    #def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:   
    
#         currentSum = sum(arr[:k-1])
#         cnt = 0
#         j = 0
#         for i,n in enumerate(arr[k-1:]):
#             if (currentSum + n) // k  >= t:
#                 cnt += 1
#             currentSum += n
#             currentSum -= arr[j]
#             j += 1 

#         return cnt
                
     def numOfSubarrays(self, a: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]
        for i in a:
            prefixSum.append(i + prefixSum[-1])
        return sum(prefixSum[i + k] - prefixSum[i] >= k * threshold for i in range(len(a) - k + 1))