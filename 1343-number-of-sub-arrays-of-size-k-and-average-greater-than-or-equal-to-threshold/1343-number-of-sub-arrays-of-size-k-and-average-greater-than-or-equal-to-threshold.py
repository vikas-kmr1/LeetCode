class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:   
    
        currentSum = sum(arr[:k-1])
        cnt = 0
    
        for i in range(k-1,len(arr)):
            if (currentSum + arr[i]) // k  >= t:
                cnt += 1
            currentSum += arr[i]
            currentSum -= arr[i-(k-1)]

        return cnt
