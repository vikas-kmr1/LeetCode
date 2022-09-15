class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2 == 1:
            return []
        
        changed.sort()
        original = []
        hashmap  = Counter(changed)
        
        for n in changed:
            if not hashmap.get(n):
                continue
            
            if not hashmap.get(n*2) :
                return []
            
            original.append(n)
            hashmap[n]-=1
            hashmap[n*2] -= 1
        
        return original
            
  