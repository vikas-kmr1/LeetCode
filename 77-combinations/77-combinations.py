class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        
        nums = [i for i in range(1, n+1)]
        ans = []
        def helper(i, cur):
            nonlocal k, nums, ans
           
            if(len(cur) == k):
              
                ans.append(cur[::])
                return
         
            for a in range(i, len(nums)):
                cur.append(nums[a])
                helper(a+1, cur)
               
                cur.pop()
              
        helper(0, [])
        return ans