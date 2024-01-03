class FrequencyTracker:

    def __init__(self):
        self.numFreq = {}
        self.freqNums = collections.defaultdict(list)

    def add(self, number: int) -> None:
        currFreq = self.numFreq.get(number,0)
        self.numFreq[number] = 1 + currFreq
        if number in self.freqNums[currFreq]:
            self.freqNums[currFreq].remove(number)
        self.freqNums[1+currFreq].append(number)

    def deleteOne(self, number: int) -> None:
        if number in self.numFreq and self.numFreq[number]>0:
            currFreq = self.numFreq[number]
            self.numFreq[number]-=1
            self.freqNums[currFreq].remove(number)
            self.freqNums[currFreq-1].append(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freqNums and len(self.freqNums[frequency]) > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

#10:0
#4:0