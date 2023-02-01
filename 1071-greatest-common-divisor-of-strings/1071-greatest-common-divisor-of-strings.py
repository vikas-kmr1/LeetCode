class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     def gcd(a: int, b: int) -> int:
    #         return b if a == 0 else gcd(b % a, a)
    #     d = gcd(len(str1), len(str2))
    #     return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''
    
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''

