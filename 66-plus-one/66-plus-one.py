class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

    
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9 :
                digits[i] = digits[i] + 1
                return digits

            if digits[i] == 9:
                digits[i] = 0
                
        if digits[0] == 0:
            digits = [1] + digits
        return digits
            
                
            
        
        # Brute-Force
#         num = 0
#         for i in digits:
#             num = (num*10)  + i
#         num += 1
#         return list(map(int,str(num).strip()))


            
        