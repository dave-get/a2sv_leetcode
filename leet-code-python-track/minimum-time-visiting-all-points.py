class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        lis=[]
        for i in range(len(points)-1):
            coun=0
            s=points[i]
            d=points[i+1]
            while (s!=d):
                if s[0]==d[0]:
                    coun+=1
                elif s[0]>d[0]:
                    s[0]-=1
                    coun+=1
                else:
                    s[0]+=1
                    coun+=1

                if s[1]==d[1]:
                    coun+=0
                elif s[1]>d[1]:
                    s[1]-=1
                else:
                    s[1]+=1
            lis.append(coun)
        v=sum(lis)
        return v