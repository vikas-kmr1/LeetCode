#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        
        # code here 

        if m==1:
            return [matrix[i][0] for i in range(n)]
        elif n == 1:
            return matrix[0]
            
        res = []
        res.extend(matrix[0])
        res.extend( [matrix[i][-1] for i in range(1,n-1)])
        res.extend(matrix[-1][::-1])
        res.extend( [matrix[i][0] for i in range(n-2,0,-1)])
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends