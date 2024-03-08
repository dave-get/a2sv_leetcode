class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.time_map[key])-1
        best = ""
        while left <= right:
            mid = (left+right)//2
            
            if self.time_map[key][mid][1] <= timestamp:
                left =mid + 1
                best = self.time_map[key][mid][0]
            else:
                right = mid - 1
        return best

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)