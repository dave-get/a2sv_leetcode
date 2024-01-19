class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right =len(skill)-1
        lis = []
        check = skill[0] + skill[right]
        for left in range(len(skill)//2):
            if check == skill[left] + skill[right]:
                lis.append(skill[left]*skill[right])
                right -=1
            else:
                return -1
        ans = sum(lis)
        return ans

