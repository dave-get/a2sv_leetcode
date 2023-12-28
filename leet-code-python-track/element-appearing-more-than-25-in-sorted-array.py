class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict_ = {num:0 for num in arr}
        lis=[]
        for i in range(len(arr)):
            if arr[i] in dict_:
                dict_[arr[i]]+=1
        for key,val in dict_.items():
            percent = (val/len(arr))*100
            if percent > 25:
                return key
        return 1