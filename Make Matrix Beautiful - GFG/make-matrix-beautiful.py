#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code her
        rm = max(sum(r) for r in matrix)
        cm = 0
        for i in range(n):
            cs = 0
            for r in range(n):
                cs += matrix[r][i]
            cm = max(cm, cs)
        return max(rm, cm)*n - sum(sum(r) for r in matrix)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends