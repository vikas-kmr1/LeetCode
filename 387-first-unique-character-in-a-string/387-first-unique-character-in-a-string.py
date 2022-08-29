class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = collections.Counter(s)
        
        for i in range(len(s)):
            if hash_map.get(s[i]) == 1:
                return i
        return -1