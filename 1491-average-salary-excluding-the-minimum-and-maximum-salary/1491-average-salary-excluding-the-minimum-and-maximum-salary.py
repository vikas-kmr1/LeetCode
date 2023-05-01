class Solution:
    def average(self, salary: List[int]) -> float:
        mxS, mnS = 0 ,inf
        agv = 0 
        for n in salary:
            agv += n
            mxS = max(mxS,n)
            mnS = min(mnS,n)
        
        return ( agv - (mxS + mnS) ) / ( len(salary) - 2 )