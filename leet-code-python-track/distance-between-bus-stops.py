class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        lis=[]
        all=sum(distance)
        if start<destination:
            y=sum(distance[start:destination])
            lis.append(y)
            lis.append(all-y)
        else:
            k=sum(distance[destination:start])
            lis.append(k)
            lis.append(all-k)
        ans = min(lis)
        return ans
        