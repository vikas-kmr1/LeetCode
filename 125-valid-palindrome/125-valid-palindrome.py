class Solution:
    def isPalindrome(self, s: str) -> bool:
        
      
        s=s.lower()
        s=s.replace(" ","")
        i = 0
        j = len(s)-1
     
        while i<j:
            if not s[i].isalnum() :
                i+=1
                continue
            if not s[j].isalnum():
                j-=1 
                continue
                
            if s[i] != s[j]:
                return False
            
            
            j-=1
            i+=1
            
                          
        return True
        
        
        