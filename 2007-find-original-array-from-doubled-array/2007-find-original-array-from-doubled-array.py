# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
        
#         if len(changed)%2 == 1:
#             return []
        
#         changed.sort()
#         original = []
#         hashmap  = Counter(changed)
        
#         for n in changed:
#             if not hashmap.get(n):
#                 continue
            
#             if not hashmap.get(n*2) :
#                 return []
            
#             original.append(n)
#             hashmap[n]-=1
#             hashmap[n*2] -= 1
        
#         return original
            
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)

        zeros, m = divmod(c[0], 2)
        if m: return []
        ans = [0]*zeros   

        for n in sorted(c.keys()):
            if c[n] > c[2*n]: return []
            c[2*n]-= c[n]
            ans.extend([n]*c[n])

        return ans