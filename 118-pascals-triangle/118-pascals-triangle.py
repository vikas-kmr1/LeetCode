class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        P_tri=[[1],[1,1]]
        
        if numRows==1:
            return P_tri[:1]
        if numRows==2:
            return P_tri[:2]
        if numRows>2:
            for i in range(2,numRows): 
                lst = []
                for j in range(0,i+1):
                    if j == 0 or j == i:
                        lst.append(1)
                    else:
                        lst.append(P_tri[i-1][j-1]+P_tri[i-1][j])
                        
                if lst:
                    P_tri.append(lst)
                    
        return P_tri

        