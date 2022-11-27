# Solution 1:
# class Solution:
#     def bestClosingTime(self, cust: str) -> int:
        
#         h = m = p = 0
#         for i, ch in enumerate(cust):       # [1] compute running profit where
#             s += (ch == "Y") * 2 - 1        #     we add +1 for Y, -1 for N
#             if s > m:                       # [2] keep track of the maximal 
#                 m, h = s, i+1               #     profit and its hour
        
#         return h                            # [3] this is the hour with minimal penalty


#Solution 2
class Solution:
    def bestClosingTime(self, c: str) -> int:
        
        n = len(c)
        no, yes = [0] * (n+1), [0] * (n+1)

        p = 0                           # [1] compute penalties for
        for i in range(n):              #     allowing no customers
            no[i] = p
            p += (c[i] == "N")          # [2] don't forget to penalize
        no[n] = p                       #     for the last hour
        
        p = 0                           # [3] compute penalties for
        for i in reversed(range(n)):    #     missing customers
            p += (c[i] == "Y")          # [4] penalty for last hour was
            yes[i] = p                  #     already correclty set to 0
        
        t = m = inf                     # [5] now scan both penalty lists
        for i in range(n+1):            #     and find the minimal one
            p = yes[i] + no[i]
            if p < m:
                m, t = p, i
        
        return t
