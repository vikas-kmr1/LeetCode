class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j)) # append destination cell to queue
                else:
                    mat[i][j]=-1  # mark -1 as unvisited
        while q:
            i, j = q.popleft()
            for (ii,jj) in ((i-1, j), (i+1, j), (i,j-1),(i,j+1)):  # four directions
				# if out of bound or has been visited, then continue
                if ii<0 or jj<0 or ii>len(mat)-1 or jj>len(mat[0])-1 or mat[ii][jj]!=-1: 
                    continue
				# current cell +1 to store distance 
                mat[ii][jj]=mat[i][j]+1
				# append new 
                q.append((ii,jj))
        return mat