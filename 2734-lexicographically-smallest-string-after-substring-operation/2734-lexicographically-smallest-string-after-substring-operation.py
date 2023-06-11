class Solution:
    def smallestString(self, s: str) -> str:
        i = 0
        while i < len(s) and s[i] == "a":
            i += 1
        if i == len(s) :
            return s[:-1]+ "z"
        ans = s[:i]
        while i < len(s) and s[i] != "a":
            ans += chr(ord(s[i])-1)
            i += 1
        return ans + s[i:]
        
     