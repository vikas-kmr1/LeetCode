class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        result = 0
        trimmed = 0
        
        s = s.strip()
         
        if s == "":
            return result
        
        if s[0] in ['-','+']:
            if s[0] == '-':
                sign = -1
            else:
                sign = +1
            s = s[1:]
                
        if (sign == 0):
            sign = 1
        
        for ch in s:
            if ch.isdigit():
                result = result*10 + int(ch)
            else:
                break
        
        return max(-2**31, min(sign * result, 2**31-1))
        