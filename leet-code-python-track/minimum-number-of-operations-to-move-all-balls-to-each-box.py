class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        count, leftCost, cos, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1': count += 1
            leftCost += count 
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': cos += 1
            rightCost += cos
            ans[i] += rightCost
        return ans