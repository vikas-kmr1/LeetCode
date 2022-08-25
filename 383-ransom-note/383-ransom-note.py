class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_hash = Counter(ransomNote)
        magazine_hash = Counter(magazine)
       
        
        for i in set(ransomNote):
           
            if ransom_hash.get(i) and magazine_hash.get(i) :
                if ransom_hash.get(i) <= magazine_hash.get(i):
                    continue
            return False
        return True
            
    
        
        
        # for i in ransomNote:
        #     if ransomNote.count(i)>magazine.count(i):
        #         return False
        # return True