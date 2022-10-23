
class Solution:
    def haveConflict(self, e1: List[str], e2: List[str]) -> bool:
          return e1[0] <= e2[1] and e2[0] <= e1[1]
        
        
        
#         event1_s = int (event1[0][:2]+event1[0][3:])
#         event1_e = int (event1[1][:2]+event1[1][3:])
#         event2_s = int (event2[0][:2]+event2[0][3:])
#         event2_e = int (event2[1][:2]+event2[1][3:])
        
#         for n in range(event2_s,event2_e+1):
#             if n in range(event1_s,event1_e+1):
#                 return True
        
#         return False
        
            
            
        

     
