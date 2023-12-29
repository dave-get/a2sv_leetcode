class OrderedStream:

    def __init__(self, n: int):
        self.Lists = [0]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.Lists[idKey-1]=value
        res = []
        for i in range( self.pointer,len(self.Lists)):
            if self.Lists[i] == 0:
                break
            self.pointer+=1
            res.append(self.Lists[i])
        return res 



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)