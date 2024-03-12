class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        _sum = 0
        def find(s,temp):
            nonlocal _sum
            if _sum == n and len(temp)==k:
                ans.append(temp[:])
                return 
            elif _sum >= n:
                return 
            seen = set()
            for i in range(s,10):
                if i not in seen:
                    _sum +=i
                    temp.append(i)
                    seen.add(i)
                    find(i+1,temp)
                    _sum -=temp.pop()
                    seen.remove(i)
        find(1,[])
        return ans

