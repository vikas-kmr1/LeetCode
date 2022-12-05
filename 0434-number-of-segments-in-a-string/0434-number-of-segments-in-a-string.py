class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(map(str,s.split())))
        