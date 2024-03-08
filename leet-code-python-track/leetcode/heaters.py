class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = []
        for i in range(len(houses)):
            x = bisect_left(heaters,houses[i])
            y = bisect_right(heaters,houses[i])-1
            if y <0:
                y = 0
            if x>=len(heaters):
                x = len(heaters)-1
            _min = min(abs(heaters[x]-houses[i]),abs(heaters[y]-houses[i]))
            ans.append(_min)
        return max(ans)

        