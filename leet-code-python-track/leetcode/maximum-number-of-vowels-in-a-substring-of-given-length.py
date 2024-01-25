class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        l = 0
        ans = 0
        dic = {"a", "e" , "i" , "o" , "u"}
        for i in range(len(s)):
            if s[i] in dic:
                count +=1
            if i >= k:
                if s[l] in dic:
                    count -=1
                l+=1
            ans = max(ans,count)
        return ans