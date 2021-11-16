import sys
import heapq 
input = sys.stdin.readline

n = int(input())
heap = []

# input이 0이면 배열에서 가장 큰 값 출력(트리의 루트 노드값 출력 = heap[0])
for i in range(n):
    num = int(input())

    # input이 자연수인 경우 힙에 값 추가
    if num != 0:
        heapq.heappush(heap, (-num, num))

    # input이 0이면 배열에서 가장 큰 값 출력(트리의 루트 노드값 출력 = heap[0]) 하면서 제거
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
        

        

# heap = []
# nums = [4,1,7,3,8,5]

# for num in nums:
#     heapq.heappush(heap, (-num, num))

# while heap:
#     print(heapq.heappop(heap)[1])
