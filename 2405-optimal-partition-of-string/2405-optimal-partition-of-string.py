class Solution:
    def partitionString(self, s: str) -> int:
        hashSet = set()
        cnt = 0
        for c in s:
            if c in hashSet:
                hashSet.clear()
                cnt += 1 
            hashSet.add(c) 
        if hashSet:
            cnt += 1
        return cnt
                