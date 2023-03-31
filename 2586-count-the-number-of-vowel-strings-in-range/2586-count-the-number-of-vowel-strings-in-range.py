class Solution:
    def vowelStrings(self, s: List[str], left: int, right: int) -> int:
        vStrs = 0
        a = ["a","e","i","o","u"]
        for i in range(left,right+1):
            if s[i][0] in a and s[i][-1] in a:
                vStrs += 1
        return vStrs
        
        