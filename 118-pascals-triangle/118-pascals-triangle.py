class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        P_tri=[[1],[1,1]]
        
        if numRows==1:
            return P_tri[:1]
        if numRows==2:
            return P_tri[:2]
        if numRows>2:
            for i in range(2,numRows):
                P_tri.append([0]*(i+1))
                P_tri[i][0]=P_tri[i][i]=1
                
                for j in range(1,i):
                    P_tri[i][j]=P_tri[i-1][j-1]+P_tri[i-1][j]
                    
                    
                    
        return P_tri

        