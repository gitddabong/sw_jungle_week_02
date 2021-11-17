# 최대 힙, 최소 힙을 구현하고
# 삽입할 때마다 최대 힙의 최댓값, 최소 힙의 최솟값을 비교해서 안맞다 싶으면 두개 위치 바꾸기
# 입력 갯수가 홀수면 최소 힙의 루트를 출력
# 입력 갯수가 짝수면 각 힙의 루트를 비교해서 더 작은놈 출력

import sys
import heapq

input = sys.stdin.readline

n = int(input())

# 최대 힙, 최소 힙 구현
max_heap = []
min_heap = []

for i in range(1, n+1):
    num = int(input())

    # i가 홀수면 최소 힙에, 짝수면 최대 힙에 삽입
    if i % 2 != 0:
        heapq.heappush(min_heap, [num, num])
    else:
        heapq.heappush(max_heap, [-num, num])

    # 삽입할 때마다 최대 힙의 최댓값, 최소 힙의 최솟값을 비교해서 안맞다 싶으면 두개 위치 바꾸기
    if min_heap and max_heap:
        if min_heap[0][1] < max_heap[0][1]: #최소힙의 루트노트가 최대힙의 루트노드보다 작으면
            maximum = heapq.heappop(max_heap)
            maximum[0] = -maximum[0]
            minimum = heapq.heappop(min_heap)
            minimum[0] = -minimum[0]

            # 두 루트노드를 자리 바꾸기
            heapq.heappush(min_heap, maximum)
            heapq.heappush(max_heap, minimum)
    
    # 입력 갯수가 홀수면 최소 힙의 루트를 출력
    if i % 2 != 0:
        print(min_heap[0][1])

    # 입력 갯수가 짝수면 각 힙의 루트를 비교해서 더 작은놈 출력
    else:
        if min_heap[0][1] > max_heap[0][1]:
            print(max_heap[0][1])
        else:
            print(min_heap[0][1])