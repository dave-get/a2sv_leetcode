class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ln = len(bookings)
        lis =[0]*(n+1)
        for i in range(ln):
            lis[bookings[i][0]-1] +=bookings[i][2]
            lis[bookings[i][1]] -=bookings[i][2]
        pref = []
        pre = 0
        for n in range(n):
            pre +=lis[n]
            pref.append(pre)
        return pref