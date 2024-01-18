from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close_nums = []
        for point in points:
            close = sqrt(pow(point[0],2) + pow(point[1],2))
            close_nums.append([close,point])
        close_nums.sort(key = lambda x: x[0])

        ans =[]
        for i in range(k):
            ans.append(close_nums[i][1])
        return ans
       
