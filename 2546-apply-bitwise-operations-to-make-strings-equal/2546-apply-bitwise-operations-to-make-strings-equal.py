class Solution:
    #solution1:
#     def makeStringsEqual(self, s: str, target: str) -> bool:
#         or_s = 0
#         or_target = 0
#         n = len(s)
#         for i in range(n):
#             or_s |= int(s[i])
#             or_target |= int(target[i])
#         return or_s == or_target
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)