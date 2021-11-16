import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
deq = deque(range(1,n+1))       # [1,2,3,4,5, .... n-1, n]

print('<', end='')
# 큐가 빌 때까지 돌리기
while deq:
    # 지우고 싶은 값 나오기 전까지 앞에것 뒤로 빼기
    for i in range(k - 1):
        deq.append(deq[0])
        deq.popleft()

    # 지울 값 pop 하면서 출력
    print(deq.popleft(), end='')

    if deq:
        print(', ', end='')

print('>')

