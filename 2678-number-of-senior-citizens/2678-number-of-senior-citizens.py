class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for d in details:
            age = int(d[-4:-2])
            if age > 60:
                cnt += 1
        return cnt 
        