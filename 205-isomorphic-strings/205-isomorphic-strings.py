class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for i in range(0, len(s)):
            hashMapS[s[i]] =  i
    
        for j in range(0, len(t)):
            hashMapT[t[j]] = j

        if list(hashMapT.values()) == list(hashMapS.values()):
        
            return True
        return False