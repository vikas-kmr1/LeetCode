class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        Fresh = 0  #count of fresh apples
        rotten = 0 # count of apples which which will be rotten
        
        
        visited=[[0 for i in range(m)]for j in range(n)]
        queue=[]
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    queue.append([i,j,0])
                    visited[i][j]=1
                if(grid[i][j]==1):
                    Fresh+=1
        if(Fresh==0):
            return 0 
        
        while queue:
                row = queue[0][0]
                col = queue[0][1]
                
                t = queue[0][2]
                queue.pop(0)
                for i,j in [(1,0),(0,1),(0,-1),(-1,0)]:
                    newRow = row+i
                    newCol = col+j
                    
                    if(newRow>=0 and newRow<n and newCol>=0 and newCol<m and grid[newRow][newCol]==1 and visited[newRow][newCol]!=1):
                        queue.append([newRow,newCol,t+1])
                        visited[newRow][newCol]=1
                        rotten+=1
        
        
        if(rotten!=Fresh):
            return -1
        return t
        