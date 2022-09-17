class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        longest_Streak = 0
        for num in hashset:
            
            if (num - 1) not in hashset:
                cur_Streak = 1
                cur_num = num
                
                while (cur_num+1) in hashset:
                    cur_num += 1
                    cur_Streak += 1
                
                
                longest_Streak = max(longest_Streak, cur_Streak)
        
        
        
        return longest_Streak
                
                
                
            
            
            
            