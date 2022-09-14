class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={"I":1,
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
        lst = 0
        for i in s[::-1]:
            n = roman.get(i)
            if  n >= lst:
                num += n
            
            else:
                num -= n
            lst = n
            
        return num
            
            
            
            

        return num    
            