class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:   
    
        currentSum = sum(arr[:k-1])
        cnt = 0
        j = 0
        for i,n in enumerate(arr[k-1:]):
            if (currentSum + n) // k  >= t:
                cnt += 1
            currentSum += n
            currentSum -= arr[j]
            j += 1 

        return cnt
                
            