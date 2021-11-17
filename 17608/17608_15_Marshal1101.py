## 17608 15 막대기 (완료)

from typing import Any
import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

class FixedStack:
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            return None
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            return None
        self.ptr -= 1
        return self.stk[self.ptr]

    def top(self):
        if self.stk[self.ptr-1] != None:
            return self.stk[self.ptr-1]
        else:
            return -1

s = FixedStack(100000)

for num in data:
    s.push(num)

first = 0
count = 1
for i in range(n):
    if i == 0:
        first = s.pop()
    else:
        if s.top() > first:
            count += 1
            first = s.pop()
        else:
            s.pop()
            

print(count)
