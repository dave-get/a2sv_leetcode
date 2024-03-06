# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        b = n
        while left <= right:
            m = (left+right)//2
            isbad = isBadVersion(m)
            if isbad:
                right = m-1
                b = m
            else:
                left = m+1
        # if isBadVersion(m):
        #     b = m
        return b