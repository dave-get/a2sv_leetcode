class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse = True)
        for decks in deck:
            queue.appendleft(decks)
            num = queue.pop()
            queue.appendleft(num)
        queue.append(queue.popleft())
        return queue