class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        count = 0
        for key,val in c.items():
            if val%2 !=0:
                count +=1
        ans = len(s)-count
        if count == 0:
            return ans
        return ans +1