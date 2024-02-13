class Solution:
    def bestClosingTime(self, customers: str) -> int:
        lis = []
        for i in customers:
            if i == "Y":
                lis.append(1)
            else:
                lis.append(0)
        sum_ = sum(lis)
        arr = []
        arr.append(sum_)
        for i in range(len(lis)):
            if lis[i] == 1:
                sum_ -=1
                arr.append(sum_)
            else:
                sum_ +=1 
                arr.append(sum_)
        m = min(arr)
        for i in range(len(arr)):
            if m == arr[i]:
                return i