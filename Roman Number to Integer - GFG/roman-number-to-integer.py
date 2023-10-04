#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        
        roman = {
            "I":  1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        prev = 0
        result = 0
        for i in s[::-1]:
            n = roman.get(i)
            
            if n >= prev:
                result += n
            
            else:
                result -= n
            
            prev = n
            
        return result
                





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends