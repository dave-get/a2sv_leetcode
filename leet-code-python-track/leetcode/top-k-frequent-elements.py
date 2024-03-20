class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        for key,val in count.items():
            buckets[val-1].append(key)
        ans = []
        for i in range(len(buckets)-1,-1,-1):
            ans.extend(buckets[i])
            if len(ans) >= k:
                return ans[:k]