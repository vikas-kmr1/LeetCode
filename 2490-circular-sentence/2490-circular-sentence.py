class Solution:
    def isCircularSentence(self, sen: str) -> bool:
        sen = list(map(str,sen.split()))
        
        if sen[0][0] == sen[-1][-1]:
            for i in range(1,len(sen)):
                if sen[i][0] != sen[i-1][-1]:
                    return False
            return True 
        
        return False
            
        