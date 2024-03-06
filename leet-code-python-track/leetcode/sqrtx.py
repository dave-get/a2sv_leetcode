class Solution:
    def mySqrt(self, x: int) -> int:
        # ans = x**(0.5)
        # return int(ans)
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid*mid > x:
                right = mid -1
            elif mid*mid < x:
                left = mid +1
            else:
                return mid
        return right