class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.val = value
        self.k = k
        self.f = 0

    def consec(self, num: int) -> bool:
        
        if len(self.stream) < self.k:
            self.stream.append(num)
            if num != self.val:
                self.f = self.k
        if len(self.stream) == self.k:
            if num != self.val:
                self.f = self.k
            self.stream.popleft()
            self.stream.append(num) 
            
            if self.f == 0:
                return True
        if self.f > 0:
            self.f -=1
            

            
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)