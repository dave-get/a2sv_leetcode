class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = 0
        s = 0
        lis = []
        while f < len(firstList) and s < len(secondList):
            if firstList[f][1] >= secondList[s][1]:
                if firstList[f][0] <= secondList[s][0]:
                    lis.append([secondList[s][0],secondList[s][1]])
                elif firstList[f][0] <= secondList[s][1]:
                    lis.append([firstList[f][0],secondList[s][1]])
                s +=1
            else:
                if firstList[f][0] >= secondList[s][0]:
                    lis.append([firstList[f][0],firstList[f][1]])
                elif firstList[f][1] >= secondList[s][0]:
                    lis.append([secondList[s][0],firstList[f][1]])
                f +=1
        return lis