class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = deque()
        index = set()
        max_len = 0
        for char in s:
            if char not in index:
                substr.append(char)
                index.add(char)
            else:
                while substr:
                    c = substr.popleft()
                    index.remove(c)
                    if c == char:
                        substr.append(char)
                        index.add(char)
                        break
            if len(substr) > max_len:
                max_len = len(substr)
        return max_len