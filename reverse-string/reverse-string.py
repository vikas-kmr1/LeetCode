def reverseString(i:int ,s:List[str]):
    if i >= len(s)//2:
        return
    reverseString(i+1,s)
    s[i],s[len(s)-i-1] = s[len(s)-i-1], s[i]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        reverseString(0,s)
        
        
        