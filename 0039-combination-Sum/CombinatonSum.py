#T.C: 2^target
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []        
        def dfs(ind,subset,total):
            if ind >= len(candidates) or total > target :
                return

            if total == target:
                res.append(subset.copy())
                return
            subset.append(candidates[ind])
            dfs(ind,subset,total + candidates[ind])

            subset.pop()
            dfs(ind+1,subset,total)

        dfs(0,[],0)
        return res

    