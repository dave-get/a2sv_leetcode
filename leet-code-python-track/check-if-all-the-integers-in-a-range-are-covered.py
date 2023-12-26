class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c=0
        for i in range(left,right+1):
            for j in range(len(ranges)):
                if i in ranges[j]:
                    c+=1
                    break
                elif i>ranges[j][0] and i<ranges[j][1]:
                    c+=1
                    break
            if c==right-left+1:
                return True
                break
        return False