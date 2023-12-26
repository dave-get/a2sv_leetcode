class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lis=[]
        m=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies < m:
                lis.append(False)
            else:
                lis.append(True)
        return lis

        