class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis_target = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            distance = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])
            if distance <= dis_target:
                return False
        return True
           
                