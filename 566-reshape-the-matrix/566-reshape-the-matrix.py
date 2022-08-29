class Solution:
      def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len = len(mat[0])
        if r * c != row_len * len(mat):
            return mat
        result = []
        for m, row in enumerate(mat):
            for n, val in enumerate(row):
                if (m * row_len + n) % c == 0:
                    result.append([])                  
                result[-1].append(val)
        return result
                
                
