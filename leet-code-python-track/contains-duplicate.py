from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        if any([val >= 2 for val in c.values()]):
            return True
        return False