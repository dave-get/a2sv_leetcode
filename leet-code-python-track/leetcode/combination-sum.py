class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lis = []
        sm = 0
        def find(temp,t,start):
            nonlocal sm,lis
            if sm == t:
                lis.append(temp[:])
                return
            if start == len(candidates) or sm > t:
                return
            for i in range(start,len(candidates)):
                temp.append(candidates[i])
                sm +=candidates[i]
                find(temp,t,i)
                sm -=candidates[i]
                temp.pop()
        find([],target,0)
        return lis