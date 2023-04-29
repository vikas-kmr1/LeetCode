class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        self.remove(s, ans, 0, 0, ['(', ')'])
        return ans
    
    def remove(self, s, ans, last_i, last_j, par):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == par[0]:
                stack += 1
            if s[i] == par[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], ans, i, j, par)
            return
        reversed_s = s[::-1]
        if par[0] == '(':
            self.remove(reversed_s, ans, 0, 0, [')', '('])
        else:
            ans.append(reversed_s)
