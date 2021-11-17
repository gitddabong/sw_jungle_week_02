# pop을 2번 시행하고 나온 수를 합치기
# 근데 pop을 2번 했을 때 힙에 수가 더 없으면 거기서 끝내면 된단 말이지?
# 그럼 무한루프 ㄱ

import sys
import heapq

input = sys.stdin.readline
testcase = int(input())

heap = []
for i in range(testcase):
    heapq.heappush(heap, int(input()))

result = 0
temp = 0
while True:
    # pop을 2번 시행하고 나온 수를 합치기
    if len(heap) > 1:
        temp = heapq.heappop(heap) + heapq.heappop(heap)
    # else:
    #     temp = heapq.heappop(heap)

    result += temp
    if not heap:
        break
    
    else:
        heapq.heappush(heap, temp)

print(result)