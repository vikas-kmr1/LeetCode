class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) 
        mat_Map = { mat[i][j] : (i,j) for i in range(m) for j in range(n) } 
        painted_rows = defaultdict(int)
        painted_cols = defaultdict(int)
        
        for it,num in enumerate(arr):
            i, j = mat_Map[num]
             
            painted_rows[i] += 1
            painted_cols[j] += 1
            
            if painted_rows[i] == n or painted_cols[j] == m:
                return it
        return -1
  