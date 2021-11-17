## 1655 25 가운데를 말해요 (완료)

import sys
import heapq
input = sys.stdin.readline

over = []
under = []
n = int(input())
for _ in range(n):
    x = int(input())
    if len(over) == len(under):
        heapq.heappush(under, (-x, x))
    else:
        heapq.heappush(over, x)
    if over != [] and over[0] < under[0][1]:
        u = heapq.heappop(under)[1]
        o = heapq.heappop(over)
        heapq.heappush(under, (-o, o))
        heapq.heappush(over, u)
    print(under[0][1])