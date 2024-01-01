class UndergroundSystem:

    def __init__(self):
        self.count = 1
        self.start_list = {}
        self.end_list = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_list[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        self.time = t - self.start_list[id][1]
        if (self.start_list[id][0],stationName) in self.end_list:
            self.end_list[(self.start_list[id][0],stationName)][0] +=self.time
            self.end_list[(self.start_list[id][0],stationName)][1] +=self.count

        else:
            self.end_list[(self.start_list[id][0],stationName)] =[self.time,self.count]
            self.count = 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans = self.end_list[(startStation,endStation)][0]/self.end_list[(startStation,endStation)][1]
        return ans

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)