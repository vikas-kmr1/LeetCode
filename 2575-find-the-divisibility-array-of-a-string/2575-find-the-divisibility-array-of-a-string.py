
    
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        x=0
        a=[0] * len(word)
        for i,n  in enumerate(word):
            x= x*10 + int(n)
            if(x%m==0):
                a[i] = 1
            x%=m
        return a