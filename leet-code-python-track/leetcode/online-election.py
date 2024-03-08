class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.person = persons
        self.time = times
        self.count= []
        self.dec = defaultdict(int)
        self.ans = []
        for i in range(len(times)):
            self.dec[persons[i]] +=1
            if not self.count:
                self.count.append([times[i],self.dec[persons[i]]])
                self.ans.append([times[i],persons[i]])

            else:
                if self.count[-1][1] <= self.dec[persons[i]]:
                    self.count.append([persons[i],self.dec[persons[i]]])
                    self.ans.append([times[i],persons[i]])
                else:
                    self.ans.append([times[i],self.count[-1][0]])
                    self.count.append([self.count[-1][0],self.count[-1][1]])

    def q(self, t: int) -> int:
        left = 0
        right = len(self.person)-1
        while left <= right:
            mid = (left+right)//2
            if self.ans[mid][0] > t:
                right = mid - 1
            elif self.ans[mid][0] < t:
                left = mid + 1
            else:
                return self.ans[mid][1]
        return self.ans[right][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)