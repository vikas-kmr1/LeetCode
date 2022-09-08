class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 =1
        rows = len(matrix)
        columns = len(matrix[0])
        
        for row in range(rows):
            if matrix[row][0] == 0:
                col0 = 0
            for column in range(1,columns):
                if matrix[row][column] == 0:
                    matrix[0][column] = matrix[row][0] = 0
                    
        for row in range(rows-1,-1,-1):
            for column in range(columns-1,0,-1):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
            if not col0:
                matrix[row][0] = 0
                
        
                    
                
    