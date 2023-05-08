class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum_  = 0
        
        for i in range(len(mat)):
            sum_ += mat[i][i]
            j = (len(mat) - i - 1 ) 
            
            if i != j:
                sum_ += mat[i][j] 
            
      
        return sum_ 
        