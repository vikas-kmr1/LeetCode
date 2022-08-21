# def reverseString(i:int ,s:List[str]):
#     if i >= len(s)//2:
#         return
#     else:
#         s[i],s[len(s)-i-1] = s[len(s)-i-1], s[i]
#         reverseString(i+1,s)
        

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         reverseString(0,s)
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        ptr1 = 0
        ptr2 = len(s)-1
        
        while ptr1 < ptr2:
            s[ptr1],s[ptr2]  = s[ptr2],s[ptr1]
            ptr1+=1
            ptr2-=1
        
        
        
        