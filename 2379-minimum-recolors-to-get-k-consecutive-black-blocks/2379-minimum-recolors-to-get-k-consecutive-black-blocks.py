class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks) - k
        cnt = blocks[0:k].count('B')
        
        for i in range(1,n+1):
            cnt = max(blocks[i:i+k].count('B') , cnt)
        
        return k - cnt
                