#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
		
		dir = [(1,0),(-1, 0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        res = 0
        n , m = len(matrix), len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                zeros = 0
                for x,y in dir:
                    if matrix[i][j] == 1 and (i + x < n and  i + x >= 0 ) and (j+y < m and j+y >= 0) and matrix[i+x][j+y] == 0:
                            zeros += 1
                
                if zeros >0 and zeros%2 == 0:
                    res += 1
        return res
                        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends