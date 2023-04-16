# class Solution:
#     def addMinimum(self, word: str) -> int:
#         it = 0
#         result = 0
#         while it < len(word) :
#             if word[it:it+3] == "abc":
#                 it += 3  
#             elif word[it:it+2] in ["ab","ac","bc"]:
#                 result += 1
#                 it += 2
#             else:
#                 result += 2
#                 it += 1
#         return result
                    
class Solution:
    def addMinimum(self, word: str) -> int:
        times = 0
        prev = 'z'
        for c in word:
            times += c <= prev
            prev = c
        return times * 3 - len(word)