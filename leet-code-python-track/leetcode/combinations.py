class Solution:
    def __init__(self):
        self.lis = []
    def combine(self, n: int, k: int) -> List[List[int]]: 
        def backtrack(start,temp):
            if k == len(temp):
                self.lis.append(temp.copy())
                return 
            for i in range(start,n+1):
                temp.append(i)
                backtrack(i+1,temp)
                temp.pop()
        backtrack(1,[])
        return self.lis