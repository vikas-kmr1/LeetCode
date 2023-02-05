class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap  = []
        for n in gifts:
            heap.append(-n)
        
        heapq.heapify(heap) 
        
        for i in range(k):
            n = heapq.heappop(heap)
            heapq.heappush(heap, -(math.floor(math.sqrt(-n))) )
        return -1*sum(heap)        
        