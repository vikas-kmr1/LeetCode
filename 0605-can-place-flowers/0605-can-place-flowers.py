class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        it = 0
        
        while it < len(f) and n:
            if not f[it]:
                next = 0 if it == len(f) - 1 else f[it + 1]
                prev = 0 if it == 0 else f[it - 1]
                
                if prev == next == 0:
                    f[it] = 1
                    n-=1
            it += 1
        return n == 0
        