class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        k=s[::-1]
        if k==s:
            return True
        else:
            return False
