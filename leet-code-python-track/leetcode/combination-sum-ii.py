class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        _sum = 0
        ans = set()
        while candidates and candidates[-1]>target:
            candidates.pop()
        def combination(s,temp):
            nonlocal _sum
            if _sum == target:
                ans.add(tuple(temp[:]))
                return
            elif _sum > target:
                return 
            seen = set()
            for i in range(s,len(candidates)):
                if candidates[i] not in seen:
                    _sum +=candidates[i]
                    temp.append(candidates[i])
                    combination(i+1,temp)
                    temp.pop()
                    _sum -=candidates[i]
                    seen.add(candidates[i])
        combination(0,[])
        return ans