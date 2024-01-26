class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        count = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if blocks[i] == "W":
                count +=1
            if i > k-2:
                ans = min(count,ans)
                if blocks[l] == "W":
                    count -=1
                l+=1
        if ans == float("inf"):
            return  0
        else:
            return ans