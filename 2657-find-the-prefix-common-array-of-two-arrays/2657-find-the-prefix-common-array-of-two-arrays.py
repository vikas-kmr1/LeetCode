class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        res = []
        seen = cur = 0
        for ab in zip(A, B):
            for a in ab:
                if (1 << a) & seen:
                    cur += 1
                seen |= 1 << a
            res.append(cur)
        return res
#         res = []
        
#         for i in range(len(A)):
#             aSet = set(A[:i+1])
#             bSet =set(B[:i+1])
#             res.append( len( aSet.intersection(bSet))  )
#         return res
        