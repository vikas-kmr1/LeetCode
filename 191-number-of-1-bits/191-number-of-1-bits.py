class Solution:
    def hammingWeight(self, n: int) -> int:
        
                
        
        
        #one line solution  95% faster
        return  bin(n).count("1")
        