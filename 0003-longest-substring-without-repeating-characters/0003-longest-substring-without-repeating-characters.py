class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:

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