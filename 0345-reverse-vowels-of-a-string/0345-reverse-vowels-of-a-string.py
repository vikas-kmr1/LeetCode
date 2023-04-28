class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [*s]
        i , j = 0 , len(s) - 1
        
        vowels = ('a','e','i','o','u')
        while i < j:
        
            while j > i and s[j].lower() not in vowels:
                j -= 1
                
            while i < j and  s[i].lower() not in vowels:
                i += 1
                
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i],s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        
        return "".join(s)
                