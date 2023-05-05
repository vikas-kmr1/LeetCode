class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        ans = 0
        
        i = 0
        cnt = 0
        a = ""
        vowels = set(['a','e','i','o','u'])
        while i < len(s):
            a += s[i]
            
            if s[i] in vowels:
                cnt += 1
            
            if len(a) == k:
                ans = max(ans,cnt)
                if a[0] in vowels:
                    cnt -= 1
                a = a[1:] 
            
                
            i += 1
            
        return ans
            
            
        