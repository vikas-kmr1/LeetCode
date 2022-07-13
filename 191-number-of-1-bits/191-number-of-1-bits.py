class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0:
            if n%2 == 1:
                c+=1
            n //=2
        return c
                
        
        
        # one line solution  95% faster
        #return  bin(n).count("1")
        