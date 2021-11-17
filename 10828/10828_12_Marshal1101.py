# 10828 12 스택 (완료) (런타임 에러 수정: 문제 입력이 최대 10000이라서 스택 갯수 10000 해야함)

import sys

n = int(sys.stdin.readline())
order_list = [list(sys.stdin.readline().split()) for _ in range(n)]

stk = [None] * 10000
ptr = 0


def empty():
    global ptr
    if ptr <= 0:
        return 1
    else:
        return 0

def push(value):
    global ptr
    stk[ptr] = value
    ptr += 1

def pop():
    global ptr
    if empty():
        return -1
    ptr -= 1
    return stk[ptr]

def size():
    global ptr
    return ptr

def top():
    global ptr
    if stk[ptr-1] != None:
        return stk[ptr-1]
    else:
        return -1

for order in order_list:
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'top':
        print(top())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'empty':
        print(empty())





# # 10828 12 스택

# from typing import Any
# import sys


# class FixedStack:
#     # __init__ 은 FixedStack을 초기를 가리킨다. FixedStack(capacity)
#     def __init__(self, capacity: int = 256) -> None:
#         self.stk = [None] * capacity
#         self.capacity = capacity
#         self.ptr = 0

#     def __len___(self) -> int:
#         return self.ptr
    
#     def is_empty(self) -> bool:
#         if self.ptr <= 0:
#             return 1
#         else:
#             return 0

#     def push(self, value: Any) -> None:
#         self.stk[self.ptr] = value
#         self.ptr += 1
    
#     def pop(self) -> Any:
#         if self.is_empty():
#             return -1
#         self.ptr -= 1
#         return self.stk[self.ptr]

#     def size(self) -> int:
#         return self.ptr

#     def top(self) -> Any:
#         if self.stk[self.ptr-1] != None:
#             return self.stk[self.ptr-1]
#         else:
#             return -1

# s = FixedStack(64)
# n = int(sys.stdin.readline())
# order_list = [list(sys.stdin.readline().split()) for _ in range(n)]

# for order in order_list:
#     if order[0] == 'push':
#         s.push(order[1])
#     elif order[0] == 'top':
#         print(s.top())
#     elif order[0] == 'size':
#         print(s.size())
#     elif order[0] == 'pop':
#         print(s.pop())
#     elif order[0] == 'empty':
#         print(s.is_empty())
    