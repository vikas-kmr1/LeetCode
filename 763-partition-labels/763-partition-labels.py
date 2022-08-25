



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #creating a hash-table that stores the last occurence of a character in string 's'
        last_occurence_table = {char: idx for idx,char in enumerate(s) }
        
        
        ans = []
        j  = 0
        lst_part = 0
        for  i,char in enumerate(s):
            j = max(j,last_occurence_table[char])
            
            if i == j:
                ans.append(j - lst_part + 1 )
                lst_part  = j+1
                
        return ans
                
            
            
        
    
                
        
        