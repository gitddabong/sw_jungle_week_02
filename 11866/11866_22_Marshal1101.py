## 11866 22 요세푸스 문제 0 (완료)

import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())

data = deque()
for i in range(n, 0, -1):
    data.append(i)

result = []
i = 0
while data:
    i -= 1
    if i % -k == 0:
        result.append(data.pop())
    else:
        data.appendleft(data.pop())

print('<', end='')
for i in range(len(result)-1):
    print(f'{result[i]}, ', end='')
print(result[-1], end='')
print('>')