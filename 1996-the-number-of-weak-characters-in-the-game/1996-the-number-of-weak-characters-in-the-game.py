class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        mxattack=properties[0][0]
        mxdefense=properties[0][1]
        count=0
        for i in range(1,len(properties)):
            if properties[i][0]<mxattack and properties[i][1]<mxdefense:
                count+=1
            else:
                mxattack=properties[i][0]
                mxdefense=properties[i][1]
        return count