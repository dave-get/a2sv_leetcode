class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = max(piles)
        while left <= right:
            mid = (left + right)//2
            sm = 0
            for i in range(len(piles)):
                sm +=ceil(piles[i]/mid)
            if sm > h:
                left = mid+1
            else:
                right = mid-1
                best = mid
        return best