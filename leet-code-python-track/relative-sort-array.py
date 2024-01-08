class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict_ = {num:[] for num in arr2}
        arr1.sort()
        for el in arr1:
            if el in dict_:
                dict_[el].append(el)
            else:
                dict_[el] = [el]
        ans = []
        for val in dict_.values():
            ans +=val
        return ans
        