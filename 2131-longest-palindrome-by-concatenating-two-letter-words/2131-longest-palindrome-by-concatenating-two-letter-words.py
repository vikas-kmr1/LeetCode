from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen= defaultdict(int)
        longest = 0
        for w in words:
            wr = w[1] + w[0]
            if wr in seen and seen[wr] > 0:
                seen[wr]-= 1
                longest+= 4
            else:
                seen[w]+= 1

        return longest + 2 if any(True for w in seen if seen[w] > 0 and w[0] == w[1]) else longest