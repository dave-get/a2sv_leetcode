class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t):
            num=num+1         
        h=num+t
        return h