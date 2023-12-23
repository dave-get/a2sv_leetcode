class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lis=[0]*len(s)
        for i in range(len(s)):
            x=indices[i]
            lis[x]=s[i]
        ans="".join(lis)
        return ans