class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        st = set(nums1) & set(nums2)
        return min(st) if len(st) else -1