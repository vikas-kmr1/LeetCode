class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #T.C : O(N+Q), where N is the length of A and Q is the number of queries
        #S.C : O(Q)O(Q), though we only allocate O(1)O(1) additional space.
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
            
            
        