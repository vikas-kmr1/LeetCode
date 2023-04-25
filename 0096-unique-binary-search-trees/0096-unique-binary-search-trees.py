
class Solution:
    def numTrees(self, n):
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)
        