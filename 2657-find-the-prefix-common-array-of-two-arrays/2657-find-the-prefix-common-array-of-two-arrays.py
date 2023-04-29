class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        
        for i in range(len(A)):
            aSet = set(A[:i+1])
            bSet =set(B[:i+1])
            res.append( len( aSet.intersection(bSet))  )
        return res
        