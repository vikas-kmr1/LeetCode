class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=list(s.split())
        return len(lst[-1])
        