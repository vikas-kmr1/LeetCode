class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0 :
            return True
        
        if len(t) == 0 or len(s) > len(t):
            return False
        
        j = 0
        for i in t:
            if j<len(s):
                if i == s[j] :
                    j+=1
        if j ==len(s):
            return True
        else:return False
            
             
    
        
            
                
    
        