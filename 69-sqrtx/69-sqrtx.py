


class Solution:
    def mySqrt(self, x: int) -> int:
        last_guess= x/2
        while True and last_guess>0:
            guess= (last_guess + x/last_guess)/2
            if abs(guess - last_guess) < .01: # example threshold
                return int(guess)
            last_guess= guess
        return 0
        
    