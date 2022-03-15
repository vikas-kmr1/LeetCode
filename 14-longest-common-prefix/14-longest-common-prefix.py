class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        k = 0 
        for i in min(strs):    
            for j in range(len(strs)):
        
                if strs[j][k] != i:
                    return prefix
            k+=1
            prefix+=i
        return prefix
                
        
        
        