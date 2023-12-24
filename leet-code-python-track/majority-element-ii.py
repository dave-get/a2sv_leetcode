class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:   
                dic[i]=1
        l=[]
        p=len(nums)/3
        for key, value in dic.items():
            if value > p:
                l.append(key)
        return l