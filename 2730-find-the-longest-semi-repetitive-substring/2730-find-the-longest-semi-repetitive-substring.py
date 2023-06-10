class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        sets = set()
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                sets.add( (i,i+1))
        pairs = 0
        for i ,j in sets:
            i -= 1
            j += 1
            counter = 0
            while i >= 0 and s[i] != s[i+1] :
                i -= 1
                counter += 1
                
            while j < len(s) and s[j] != s[j-1]:
                j += 1
                counter += 1
            pairs = max(pairs ,2+counter)
        return pairs if  pairs else len(s)
        
        