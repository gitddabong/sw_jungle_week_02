## 13334 27 철로 ()

import sys, heapq

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    h, o = map(int,input().split())
    if h > o:
        data.append([o, h])
    else:
        data.append([h, o])
d = int(input())
arr = []
for i in range(n):
    if data[i][1] - data[i][0] <= d:
        arr.append(data[i])

arr.sort(key=lambda x:x[1])

heap = []
maxc = 0
for x in arr:
    if heap == []:
        heapq.heappush(heap, x)
    else:
        while heap != [] and heap[0][0] + d < x[1]:
            heapq.heappop(heap)
        heapq.heappush(heap, x)
    maxc = max(maxc, len(heap))
print(maxc)