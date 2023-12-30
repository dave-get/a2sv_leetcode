from collections import Counter
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        st = set()
        for i in range(len(backs)):
            if backs[i]==fronts[i]:
                st.add(fronts[i])
        ans = float('inf')
        for num in (fronts + backs):
            if num not in st:
                ans = min(ans,num)       
        if ans!=float('inf'):
            return ans           
        else:
            return 0