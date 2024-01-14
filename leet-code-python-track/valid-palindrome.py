class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in range(len(s)):
            if s[i].isalnum():
                ans +=s[i].lower()
        r = len(ans)-1
        print(ans)
        for i in  range(len(ans)//2):
            if ans[i] != ans[r]:
                return False
                break
            r -=1
        return True