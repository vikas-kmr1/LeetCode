import collections
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq = collections.Counter(skill) 
        res = []
        avg = sum(skill)//(len(skill)//2)
        for i in range(len(skill)):
            n = avg - skill[i]
            if freq.get(skill[i]):
                freq[skill[i]] = freq.get(skill[i])-1
                if freq.get(n):
                    res.append((skill[i],n))
                    freq[n] = freq.get(n) - 1
                    
        if len(res) != len(skill)//2:
            return -1
        
        ans = 0
        for a,b in res:
            ans+= (a*b)
            
        return ans
        