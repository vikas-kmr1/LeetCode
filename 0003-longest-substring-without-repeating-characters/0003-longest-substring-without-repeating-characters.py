class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charset = set()
        max_len = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
           
            charset.add(s[r])
            max_len = max(r - l + 1,max_len)
            
        return max_len
                
        