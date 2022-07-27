class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if sorted(s) == sorted(t):
            return True
        return False
        
        
        
#         if len(s)==len(t):
#             for i in s:
#                 if s.count(i)!=t.count(i):
#                     return False
                
    
#             return True
                
#         else: return False