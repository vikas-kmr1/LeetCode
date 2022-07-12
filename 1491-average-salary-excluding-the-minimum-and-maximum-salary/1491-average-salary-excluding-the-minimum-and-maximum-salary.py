class Solution:
    def average(self, salary: List[int]) -> float:
       
        salary.remove(min(salary))
        salary.remove(max(salary))
        print(salary)
        
        return sum(salary)/len(salary)
        