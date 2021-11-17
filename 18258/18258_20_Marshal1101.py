## 18258 20 큐 2 (시간초과)

from typing import Any
import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(sys.stdin.readline().split()))

no = 0
front = 0
rear = 0
capacity = 2000000
que = [None] * capacity


def push(x):
    global rear
    global no
    que[rear] = x
    rear += 1
    no += 1
    if rear == capacity:
        rear = 0    

def pop():
    global front
    global no
    if no > 0:
        x = que[front]
        front += 1
        no -= 1
        if front == capacity:
            front = 0
        return x

    if no <= 0:
        return -1

def size():
    global no
    return no

def empty():
    global no
    if no <= 0:
        return 1
    else:
        return 0

def peek_front():
    global front
    if que[front] == None:
        return -1
    else:
        return que[front]

def peek_rear():
    global rear
    if que[rear-1] == None:
        return -1
    else:
        return que[rear-1]

for order in data:
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(peek_front())
    elif order[0] == 'back':
        print(peek_rear())


# from typing import Any

# import sys


# class FixedQueue:

#     class Empty(Exception):
#         ## 비어 있는 큐에서 디큐 또는 피크할 때 내보내는 예외 처리
#         pass

#     class Full(Exception):
#         ## 가드 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리
#         pass

#     def __init__(self, capacity: int) -> None:
#         self.no = 0
#         self.front = 0
#         self.rear = 0
#         self.capacity = capacity
#         self.que = [None] * capacity

#     def __len__(self) -> int:
#         return self.no

#     def is_empty(self) -> bool:
#         return self.no <= 0

#     def is_full(self) -> bool:
#         return self.no >= self.capacity

#     def enque(self, x: Any) -> None:
#         if self.is_full():
#             return FixedQueue.Full
#         self.que[self.rear] = x
#         self.rear += 1
#         self.no += 1
#         if self.rear == self.capacity:
#             self.rear = 0

#     def deque(self) -> Any:
#         if self.is_empty():
#             return FixedQueue.Empty
#         x = self.que[self.front]
#         self.front += 1
#         self.no -= 1
#         if self.front == self.capacity:
#             self.front = 0
#         return x

#     def peek(self) -> Any:
#         if self.is_empty():
#             raise FixedQueue.Empty
#         return self.que[self.front]

#     def find(self, value: Any) -> Any:
#         for i in range(self.no):
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:
#                 return idx
#         return -1
    
#     def count(self, value: Any) -> bool:
#         c = 0
#         for i in range(self.no):
#             idx = (i + self.front) % self.capacity
#             if self.que[idx] == value:
#                 c += 1
#         return c

#     def __contains__(self, value: Any) -> bool:
#         return self.count(value)

#     def clear(self) -> None:
#         self.no = self.front = self.rear = 0

#     def dump(self) -> None:
#         if self.is_empty():
#             print('큐가 비었습니다.')
#         else:
#             for i in range(self.no):
#                 print(self.que[(i + self.front) % self.capacity], end='')
#             print()

