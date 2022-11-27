class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tpt,spt = 0,0
        
        while spt < len(s) and tpt < len(t):
            if s[spt] == t[tpt]:
                tpt += 1
            spt += 1
        return len(t) - tpt
        