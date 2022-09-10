class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        
        
        #transpose matrix first:
        
        for i in range(n):
            for j in range(i+1,n):
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
                
            
        # now reverese each column of the matrix:
        
        for col in matrix:
                i = 0 
                j = n-1
                
                while i < j:
                    col[i],col[j] = col[j],col[i]
                    i+= 1
                    j-=1
        
                    
                
                
        
        
        
        
        # for i in range(n // 2 + n % 2):
        #     for j in range(n // 2):
        #         tmp = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        #         matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
        #         matrix[j][n - 1 - i] = matrix[i][j]
        #         matrix[i][j] = tmp