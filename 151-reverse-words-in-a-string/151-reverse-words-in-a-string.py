class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        left = 0 
        right = len(s) - 1
        temp = ""
        ans = ""

        
        while left <= right:
            
            if s[left] != " ":
                temp += s[left]
                
            
            if s[left] == " " and temp != "":
                ans = " " + temp + ans
                temp = ""
            left += 1
            
        if temp != "":
            ans = temp + ans
          
        return ans
                
            
            
                
                
        