class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = ""
        t = 0
        for i in s:
            if i not in l:
                l+=i
            else:
                l = l.split(i)[1]+i
                
            if len(l)>t:
                t = len(l)
        return t