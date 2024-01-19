class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greed = 0
        size = 0
        ans = 0
        count =0
        while greed < len(g) and size < len(s):
            if s[size] >= g[greed]:
                count +=1
                size +=1
                greed +=1
            else:
                size +=1
            ans = max(ans,count)
            
        print(ans)
        return ans
            