class Solution:
    def strStr(self, h: str, n: str) -> int:
        
        i = 0
        while i <= len(h)- len(n):
            if h[i:i+len(n)] == n:
                return i
            i+=1
        return -1
            
        
        
#         if needle in haystack:
#             return haystack.find(needle)
#         return -1
            
        
        