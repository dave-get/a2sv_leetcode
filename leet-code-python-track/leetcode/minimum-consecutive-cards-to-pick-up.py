class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = defaultdict(int)
        ans = len(cards)+1
        left = 0
        for right in range(len(cards)):
            count[cards[right]] +=1
            if count[cards[right]] > 1:
                while count[cards[right]] > 1:
                    ans = min(ans,right-left+1)
                    count[cards[left]] -=1
                    left +=1
        if ans == len(cards)+1:
            return -1
        return ans
