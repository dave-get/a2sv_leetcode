class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        c = set(s)
        print(s)
        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                return max(self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:]),key=len)
        return s
