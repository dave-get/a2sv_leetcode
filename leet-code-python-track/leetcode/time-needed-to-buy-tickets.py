class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = []
        for i in range(len(tickets)):
            if tickets[i] - tickets[k] < 0:
                que.append(tickets[i])
            else:
                if i > k:
                    que.append(tickets[k]-1)
                else:
                    que.append(tickets[k])
        print(que)
        print(tickets[k])
        return sum(que)