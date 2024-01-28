class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ln = len(trips)
        trips.sort(key = lambda x: x[1])
        lis_len = max(trips,key = lambda x: x[2])[2]
        lis = [0]*(lis_len+1)
        for i in range(ln):
            lis[trips[i][1]] +=trips[i][0]
            lis[trips[i][2]] -=trips[i][0]
        pre = 0
        for i in range(len(lis)):
            lis[i] +=pre
            pre =lis[i]
        for num in trips:
            if lis[num[1]] > capacity:
                return False
        return True