## T.C: O(n)
## S.C: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        
        count = [[] for _ in range(len(nums)+1)] 

        for key,val in freq.items():
            count[val].append(key)
            
        res = []
        for lst in count[::-1]:
            res.extend(lst)
            if len(res) == k:
                return res
        


        





        