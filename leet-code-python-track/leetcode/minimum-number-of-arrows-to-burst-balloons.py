class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[1])
        
        print(points)
        c = points[0][1]
        count =0
        for i in range(1,len(points)):
            if points[i][0] > c:
                count +=1
                c = points[i][1]
        return count+1