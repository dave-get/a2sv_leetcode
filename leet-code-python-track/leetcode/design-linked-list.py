class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None 

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        temp = self.head
        count_index = 0
        while temp.next:
            if count_index == index:
                break
            count_index +=1 
            temp = temp.next
        if index == count_index:
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            return 
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        temp = self.head
        if not self.head:
            self.addAtHead(val)
        else:
            while temp.next:
                temp = temp.next
            temp.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        if index == 0:
            self.addAtHead(val)
            return
        elif not self.head:
            return
        elif index == 1:
            node.next = self.head.next
            self.head.next = node
            return
        temp1 = self.head
        temp2 = self.head.next
        count_index = 1
        while temp2 and temp2.next:
            if count_index == index:
                break
            count_index +=1 
            temp1 = temp1.next
            temp2 = temp2.next
        if index <= count_index:
            node.next = temp2
            temp1.next = node
            return
        if index - count_index == 1:
            temp2.next = node
            return

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        elif index == 0:
            self.head = self.head.next
            return
        temp1 = self.head
        temp2 = self.head.next
        count_index = 1
        while temp2 and temp2.next:
            if count_index == index:
                break
            count_index +=1
            temp1 = temp1.next
            temp2 = temp2.next
        if index <= count_index:
            if temp2:
                temp1.next = temp2.next
            return
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)