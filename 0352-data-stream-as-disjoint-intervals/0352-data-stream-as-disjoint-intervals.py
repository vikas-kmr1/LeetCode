class SummaryRanges:
    def __init__(self):
        self.seen=set()

    def addNum(self, val: int) -> None:
        self.seen.add(val)

    def getIntervals(self) -> List[List[int]]:
        res=[]
        for v in sorted(self.seen):
            if not res or v>res[-1][1]+1:
                res.append([v,v])
            elif res and v==res[-1][1]+1:
                res[-1][1]=v
        return res