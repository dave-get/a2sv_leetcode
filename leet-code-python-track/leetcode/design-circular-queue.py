class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = ['']*k
        self.size = k
        self.rear = 0
        self.front = 0

    def enQueue(self, value: int) -> bool:
        if self.rear < self.size and self.queue[self.rear] == '':
            self.queue[self.rear] = value
            self.rear +=1
            # print("rear: ",self.rear)
            # print(self.queue)
            return True
        if self.rear == self.size and self.queue[0] == '':
            self.queue[0] = value
            self.rear = 1
            # print("rear: ",self.rear)
            # print(self.queue) 
            return True
        return False

    def deQueue(self) -> bool:
        if  self.front < self.size and self.queue[self.front] !='':
            self.queue[self.front] = ''
            self.front +=1
            if self.front == self.size:
                self.front = 0
            # print("front: ",self.front)
            # print(self.queue)
            return True
        
        return False

    def Front(self) -> int:
        if self.queue[self.front] != '':
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if self.queue[self.rear-1] != '':
            return self.queue[self.rear-1]
        return -1
        
    def isEmpty(self) -> bool:
        if self.rear == self.size:
            if self.queue[0] == '' and self.queue[self.front] == '':
                return True
        if self.queue[self.rear] == '' and self.queue[self.front] == '':
            return True
        return False
        
    def isFull(self) -> bool:
        if self.rear == self.size:
            if self.queue[0] != '' and self.queue[self.front] != '':
                return True
        if self.queue[self.rear] != '' and self.queue[self.front] != '':
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()