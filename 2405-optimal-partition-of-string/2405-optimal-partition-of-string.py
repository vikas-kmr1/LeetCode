class Solution:
    def partitionString(self, s: str) -> int:
        hashSet = set()
        cnt = 0
        for c in s:
            if c in hashSet:
                hashSet.clear()
                cnt += 1 
            hashSet.add(c) 
        if hashSet:
            cnt += 1
        return cnt
# class Solution:
#     def partitionString(self, s: str) -> int:
#         i, ans, flag = 0, 1, 0
#         while i < len(s):
#             val = ord(s[i]) - ord('a')
#             if flag & (1 << val):
#                 flag = 0
#                 ans += 1
#             flag |= 1 << val
#             i += 1
#         return ans
                