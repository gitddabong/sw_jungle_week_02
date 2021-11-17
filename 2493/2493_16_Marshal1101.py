## 2493 16 탑

import sys
from typing import Sequence


n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

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

s = FixedStack(500000)
arrive = []


def laser_top(data):
    arrive.append(0)
    s.push([data[0], 1])
    i = 1
    while i < n:
        if s.top()[0] > data[i]:
            arrive.append(s.top()[1])
            s.push([data[i], i+1])
            i += 1
        else:
            while True:
                if s.top() == -1:
                    arrive.append(0)
                    s.push([data[i], i+1])
                    break
                elif s.top()[0] > data[i]:
                    arrive.append(s.top()[1])
                    s.push([data[i], i+1])
                    break
                else:
                    s.pop()
            i += 1
            
laser_top(data)
print(*arrive)