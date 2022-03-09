class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000,
             "IV":4,
             "IX":9,
             "XL":40,
             "XC":90,
             "CD":400,
             "CM":900
            
        }
        num=0
        i=0
        while(i<len(s)):
            
            if ((i<(len(s)-1))) and( s[i:i+2]=='IV' or  s[i:i+2]=='IX' or s[i:i+2]=="XL" or s[i:i+2]=="XC" or s[i:i+2]=="CD" or s[i:i+2]=="CM"):
                num+=dic.get(s[i:i+2])
                print(dic.get(s[i:i+2]))  
                i+=1
            else:
                num+=dic.get(s[i])
                print(dic.get(s[i]))
            i+=1
        return num    
            