class Solution:
    def reverseVowels(self, s):
        VOWELS: set = { "a", "e", "i", "o", "u", "A", "E", "I", "O", "U" }
            
        characters: list[str] = list(s)
        left, right = 0, len(characters) - 1
        while left < right:
            left_value, right_value = characters[left], characters[right]
            if left_value in VOWELS and right_value in VOWELS:
                characters[left], characters[right] = characters[right], characters[left]
                left += 1
                right -= 1
            elif left_value in VOWELS and right_value not in VOWELS:
                right -= 1
            elif left_value not in VOWELS and right_value in VOWELS:
                left += 1
            else:
                left += 1
                right -= 1
        
        return "".join(characters)