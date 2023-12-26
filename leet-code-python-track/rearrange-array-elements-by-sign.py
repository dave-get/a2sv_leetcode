class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lis1=[]
        lis2=[]
        lis3=[]
        for i in nums:
            if i<0:
                lis1.append(i)
            else:
                lis2.append(i)
        for i in range(max(len(lis1),len(lis2))):
            if i<len(lis2):
                lis3.append(lis2[i])
            if i<len(lis1):
                lis3.append(lis1[i])
        return lis3
