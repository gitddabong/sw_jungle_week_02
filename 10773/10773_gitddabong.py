import sys
from collections import deque

input = sys.stdin.readline
testcase = int(input())
deq = deque()

for i in range(testcase):
    n = int(input())

    # 0이 아니면 수를 저장, 0이면 수를 삭제
    # 정수가 0일 경우에 지울 수 있는 수가 보장된다는 뜻은
    # 수를 확실하게 지울 수 있을 때만 0을 준다는 뜻
    if n != 0:
        deq.append(n)
    else:
        deq.pop()

print(sum(deq))
