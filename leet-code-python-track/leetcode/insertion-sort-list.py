# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lis = ListNode()
        dummy = lis.next
        while temp:
            current = temp
            temp = current.next
            current.next = dummy
            dummy = current
            b1 = current.next
            b2 = dummy
            while b1 and b2 and b1.val < b2.val:
                ch = b2.val
                b2.val = b1.val
                b1.val = ch

                b1 = b1.next
                b2 = b2.next
        # print(dummy)
        return dummy
        