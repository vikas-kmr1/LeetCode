class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        cntL = 0
        cntR = 0
        vowels = {
                 "A" : 1,
                 "a" : 1,
                 "E" : 1,
                 "e" : 1,
                 "I" : 1,
                 "i" : 1,
                 "O" : 1,
                 "o" : 1,
                 "U" : 1,
                 "u" : 1
                 }
        
        for i in range(n//2):
            if vowels.get(s[i]):
                cntL += 1
            if vowels.get(s[i+n//2]):
                cntR += 1
        return cntL == cntR
    