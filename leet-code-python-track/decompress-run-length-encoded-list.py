class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]: 

        ln=int(len(nums)/2)
        k=0
        lis=[]
        for i in range(0,ln):
            h=nums[k:k+2]
            k=k+2
            for j in range(h[0]):
                lis.append(h[1])
        return lis