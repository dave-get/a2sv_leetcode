class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        down = False
        dic = 0
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                if down:
                    return False
                    break
            elif arr[i-1] == arr[i]:
                return False
                break
            elif arr[i-1] > arr[i]:
                if i ==1:
                    return False
                    break
                down = True
                dic +=1
        if len(arr)==1 or dic==0:
            return False
        return True