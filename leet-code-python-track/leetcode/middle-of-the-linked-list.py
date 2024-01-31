# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        while temp1 and temp1.next:
            temp1 = temp1.next.next
            temp2 = temp2.next
        # arr = []
        # while temp1 != temp2:
        #     arr.append(temp1.val)
        #     temp1 = temp1.next
        return temp2