class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.time = timeToLive
        self.dic = defaultdict(int)

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.dic[tokenId] = currentTime
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        print(self.dic)
        if tokenId in self.dic:
            if currentTime >= self.dic[tokenId] + self.time:
                del self.dic[tokenId]
            else:
                self.dic[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        count =0
        for key,val in self.dic.items():
            if currentTime >= self.dic[key] + self.time:
                del self.dic[key]
            if key in self.dic:
                count +=1
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)