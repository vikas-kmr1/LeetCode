# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
            lt , rt = 1 , n
            while lt < rt:
                pivot_version = lt + (rt - lt)//2
            
                if (isBadVersion(pivot_version)):
                    rt = pivot_version
                else:
                    lt = pivot_version + 1 
                
            return rt # can return lt as well both are same
                
    
            
        
                
                
        
        