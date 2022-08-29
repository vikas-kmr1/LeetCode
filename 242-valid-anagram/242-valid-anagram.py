class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = Counter(s)
        hash_map_t = Counter(t)
        
        if hash_map_s == hash_map_t:
            return True
        
        return False
        
        
        
        
#         if len(s)==len(t):
#             for i in s:
#                 if s.count(i)!=t.count(i):
#                     return False
                
    
#             return True
                
#         else: return False