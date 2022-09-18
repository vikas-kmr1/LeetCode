class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        
# 		# Window start
#         windowStart = 0
        
# 		# Stores the indices of each character
#         char_indices = {}
        
#         max_len = 0
        
		
#         for windowEnd in range(len(s)):
				
# 			# Right end of window
#             right_char = s[windowEnd]
            
# 			# Check if current character already in window
#             if right_char in char_indices:
                
# 				# Update the windowStart to the max of current windowStart index and 1 right to the current characters previous index
#                 windowStart = max(windowStart, char_indices[right_char] + 1)
            
# 			# Keep track of the index of the current char on window end
#             char_indices[right_char] = windowEnd
            
# 			# Keep track of the max lenght of the unique substring with unique characters
#             max_len = max(max_len, windowEnd - windowStart + 1)
        
#         return max_len

        
        #T.c: O(N)
        #S.C: O(N)
        charset = set()
        max_len = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_len = max(max_len, r - l +1)
    
        return max_len