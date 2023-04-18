class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        i = 0
        j = 0
        
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
            
        res += word1[i:] if i < len(word1) else word2[j:]
        
        return res
        