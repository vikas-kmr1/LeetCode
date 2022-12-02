class Solution:
   def closeStrings(self, word1: str, word2: str) -> bool:
        l1, l2 = len(word1), len(word2)
        
        if l1 != l2:    return 0     #if lengths not match then reject
        
        unique_1 = Counter(word1)     #count freq {'a': 1, 'b': 2}
        unique_2 = Counter(word2)
        
		#now, check if each character is present in both words
        for ch in unique_1.keys():
            if ch not in unique_2.keys():
                return 0 
		#okay, so each charater is present now check if each character's freq is also same
		# okay case is {'a': 5, 'b': 2, 'c': 2}
		# Not okay case is {'a': 3, 'b': 4, 'c': 2}  because even thogh each
		# character is present and total char count is also same still chars are not interchangeble
        freq1 = Counter(unique_1.values()) # count freq of each freq 
        freq2 = Counter(unique_2.values())
        
		# check freq counts
        for f, v in freq1.items():
            if freq2[f] != v:
                return 0
        
        return 1