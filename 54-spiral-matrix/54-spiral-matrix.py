class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # T.C: O(m*n) where m is no. of rows and n is the no. of columns 
        # S.C: O(m*n) if does include the output space else O(1)
        res = []
        left, right = 0 , len(matrix[0])
        top, bottom = 0 , len(matrix)
        
        while left < right and top < bottom:
            #get every ith element in top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            
            #get every i element in right column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            #get every ith element in bottom row:
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # get every ith element in left column:
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left += 1
            
        return res
            
            
            
            
                
            
        
        
