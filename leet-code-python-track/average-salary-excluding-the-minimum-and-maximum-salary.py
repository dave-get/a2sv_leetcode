class Solution:
    def average(self, salary: List[int]) -> float:
        x=min(salary) 
        y=max(salary) 
        salary.remove(x) 
        salary.remove(y)
        d=sum(salary)/len(salary)
        return d