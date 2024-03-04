class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded_set = set()
        wall_set = set([tuple(a) for a in walls])
        guard_set = set([tuple(a) for a in guards])

        for x, y in guards:
            a,b = x, y
            x, y = a, b+1
            #move down
            while x < m and y < n and (x, y) not in wall_set and not (x, y) in guard_set:
                guarded_set.add((x, y))
                y = y+1
            #move up
            x,y = a, b-1
            while x < m and y >= 0 and (x, y) not in wall_set and not (x, y) in guard_set:
                guarded_set.add((x, y))
                y = y-1
            #move left
            x, y = a-1, b
            while x >= 0 and y < n and (x, y) not in wall_set and not (x, y) in guard_set:
                guarded_set.add((x, y))
                x = x-1
            #move right
            x, y = a+1, b
            while x < m and y < n and (x, y) not in wall_set and not (x, y) in guard_set:
                guarded_set.add((x, y))
                x = x+1
        return m*n - len(guarded_set) - len(walls) - len(guards)