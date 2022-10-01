from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        # [1] count letter frequencies
        freq = Counter(word)
        
        # [2] check several frequency conditions
        
        #     - for a single unique letter in the word
        if  len(freq.most_common()) == 1:
            return True

        #     - for all frequencies being equal to 1
        if  freq.most_common()[0][1] == 1:
            return True

        #     - for one most frequent element
        if  freq.most_common()[0][1] - freq.most_common()[1][1] == 1 and freq.most_common()[1][1] == freq.most_common()[-1][1]:
                return True

        #     - for one less frequent element
        if  freq.most_common()[-2][1] - freq.most_common()[-1][1] == 1 and freq.most_common()[0][1] == freq.most_common()[-2][1]:
                return True
                
        return False