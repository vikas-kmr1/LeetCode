class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = sum(n for n in nums if n%2 == 0)
        ans = []
        
        for val, ind in queries:
            if nums[ind] % 2 == 0:
                even_sum -= nums[ind]
            
            nums[ind] += val
            
            if nums[ind]%2 == 0:
                even_sum += nums[ind]
            
            ans.append(even_sum)
            
        return ans
            
            
        