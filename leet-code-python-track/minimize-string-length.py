class Solution:
    def minimizedStringLength(self, s: str) -> int:
        st=set(s)
        ans = len(st)
        return ans