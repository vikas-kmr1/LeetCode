def getRev(x,res):
# using recustion
#     if x>0:
#         res = (res * 10) + (x%10)
#         return getRev(x//10 , res )
    
#     if (res >= (2**31) - 1) or (res <= (2**31) * -1):
#         return 0
    
#     else:return res

    while x>0:
        res = (res * 10) + (x%10)
        if (res >= (2**31) - 1) or (res <= (2**31) * -1):
            return 0
        x= x//10  
    return res




class Solution:
    def reverse(self, x: int) -> int:
        
        if (x > (2**31) - 1) or (x < (2**31) * -1):
            return 0
        
        else:    
            signMultiplier = 1
            if x < 0:
                signMultiplier = -1
                x = x * -1
            
            revNum = getRev(x,0)
            
            return signMultiplier * revNum
        