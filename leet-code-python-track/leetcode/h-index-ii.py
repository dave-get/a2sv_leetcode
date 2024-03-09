class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def search(m):
            left = 0
            right = len(citations)
            ind = 0
            while left <= right:
                mid = (left+right)//2
                if m <= citations[mid]:
                    ind = mid
                    right =mid - 1
                else:
                    left =mid + 1
            if len(citations[ind:]) >= m:
                return True
            return False
        ans = 0
        left = 0
        right = max(citations)
        while left <= right:
            mid = (left+right)//2
           
            if search(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans