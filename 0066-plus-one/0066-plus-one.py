class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:

            n  = (digits[i] + carry) 
            carry = (n // 10)
            digits[i] = n % 10
            i -= 1

        if carry:
            digits = [carry] + digits
        return digits

    
#     class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

    
#         for i in range(len(digits)-1,-1,-1):
#             if digits[i] != 9 :
#                 digits[i] = digits[i] + 1
#                 return digits

#             if digits[i] == 9:
#                 digits[i] = 0
                
#         if digits[0] == 0:
#             digits = [1] + digits
#         return digits
        