## 2164 21 카드2 (완료)
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

result = deque()
for i in range(n, 0, -1):
    result.append(i)

def card():
    i = n
    while i > 1:
        result.pop()
        i -= 1
        x = result.pop()
        result.appendleft(x)
    print(result[0])

card()