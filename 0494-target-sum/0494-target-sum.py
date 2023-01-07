class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def backTrack(i:int, s:int)->int:
            if i == len(nums):
                return 1 if s == target else 0
            
            if (i,s) in dp:
                return dp.get((i,s),0)
            
            dp[(i,s)] =  backTrack(i+1, s + nums[i]) + backTrack(i+1, s - nums[i])
            return dp[(i,s)]
        return backTrack(0,0)
    
                
        
# brute-Force:
# gives TLE      
#         cnt = 0
#         def backTrack(i:int, s:int):
#             nonlocal cnt
#             if i == len(nums):
#                 if s == target:
#                     cnt += 1
#             else:
#                 backTrack(i + 1 , s + nums[i])
#                 backTrack(i + 1 , s - nums[i])
#         backTrack(0,0)
#         return cnt
                    
            