class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq.items(), key= lambda x:x[1],reverse = True)
        return [freq[i][0] for i in range(k)]
        