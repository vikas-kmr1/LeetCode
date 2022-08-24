import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n>0:
            return (log10(n)/log10(3)).is_integer()
        return False
      