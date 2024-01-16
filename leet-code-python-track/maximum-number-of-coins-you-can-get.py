class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        left = sum_ = 0
        right=len(piles)-2
        while left < right:
            sum_ += sorted_piles[right]
            left +=1
            right -=2
        return sum_ 

