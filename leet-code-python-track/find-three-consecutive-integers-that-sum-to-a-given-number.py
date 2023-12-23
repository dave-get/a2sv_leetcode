class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        for i in range(3):
            con=int((num-3)/3)
            if con+con+1+con+2==num:
                return [con,con+1,con+2]
            else:
                return []