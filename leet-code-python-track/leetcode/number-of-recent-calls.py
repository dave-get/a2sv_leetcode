class RecentCounter:

    def __init__(self):
        self.queue = []
        self.c = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - 3000 > self.queue[self.c]:
            self.c +=1
        return len(self.queue) - self.c


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)