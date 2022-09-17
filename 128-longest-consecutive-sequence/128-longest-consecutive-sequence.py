#T.C: O(n)
#S.C: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums) # add all distinct nums in hashset
        longest_Streak = 0  # initial streak = 0
        for num in hashset: 
            
            if (num - 1) not in hashset: # if num - 1 not present in hashset, then
                cur_Streak = 1 # i.e num is in hashset
                cur_num = num 
                
                while (cur_num+1) in hashset: # now search untill current num + 1 is in hashset 
                    cur_num += 1 # increment current num by +1
                    cur_Streak += 1 # also increment current streak by +1
                
                
                longest_Streak = max(longest_Streak, cur_Streak)# now check max b/w last and current streak
        
        return longest_Streak
                
                
                
            
            
            
            