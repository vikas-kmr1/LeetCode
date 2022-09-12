class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        ans = 0
        score = 0
        while r >= l:
            if P >= tokens[l]:
                score += 1
                P -= tokens[l]
                l += 1
                ans = max(ans, score)
            elif P < tokens[l] and score > 0:
                score -= 1
                P += tokens[r]
                r -= 1
            else:
                return ans
        return ans