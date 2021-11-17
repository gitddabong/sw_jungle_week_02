## 1715 26 카드 정렬하기

import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

count = 0
while True:
    if len(heap) == 1:
        break
    new = heapq.heappop(heap) + heapq.heappop(heap)
    count += new
    heapq.heappush(heap, new)
print(count)