class Solution:
    def climbStairs(self, n: int) -> int:
#         one  = 1
#         two  = 1
        
#         for i in range(1,n):
#             temp = one
#             one = one + two
#             two = temp
#         return one
   
    #memorize 
        cache ={}
        cache[1] = 1
        cache[2] = 2
        def climb(m):
            if m in cache:
                return cache[m] 
            cache[m] = climb(m -1) + climb(m-2)
            return cache[m]
        return climb(n)
    
# recursive (TLE) #T.C: O(2^n)

#         cnt = 0
#         def helper(step):
#             nonlocal cnt
#             if step > n:
#                 return
#             if step == n:
#                 cnt +=1  
#             helper(step+1)
#             helper(step+2)
            
#         helper(0)
#         return cnt
            
        