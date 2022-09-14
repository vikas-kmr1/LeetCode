class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.res = ""
        self.resLen = 0
                
        
        for i in range(len(s)):
            #odd len palindrome
            res =self.expandCenter(s,i,i)

            #even len palindrome
            self.expandCenter(s,i,i+1)
                          
        return self.res
            
    def expandCenter(self,s, left:int, right:int):
           
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                if self.resLen < (right -left +1):
                    self.resLen = (right -left +1)
                    self.res = s[left:right+1]
                    
                
                left -= 1
                right += 1            
        