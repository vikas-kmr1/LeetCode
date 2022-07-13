class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i,j = 0,0
        while i<len(s) and j <len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
      
        return i==len(s)
        
        
        
        
        
        
        
        
        
        # 96.87% faster
        
#         if len(s) == 0 :
#             return True
        
#         if len(t) == 0 or len(s) > len(t):
#             return False
        
#         j = 0
#         for i in t:
#             if j<len(s):
#                 if i == s[j] :
#                     j+=1
#         if j ==len(s):
#             return True
#         else:return False
            
             
    
        
            
                
    
        