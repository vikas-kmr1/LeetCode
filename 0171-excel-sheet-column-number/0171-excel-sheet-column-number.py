class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        col_no = 0
        
        for c in columnTitle:
        
            col_no = (col_no * 26) + (ord(c) - ord('A') + 1)
        
        return col_no
        