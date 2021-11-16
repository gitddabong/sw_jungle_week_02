import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

n = int(input())

for _ in range(n):
    string_ = list(input().split())
    
    if string_[0] == 'push':
        deq.append(string_[1])

    elif string_[0] == 'pop':
        # 큐가 비어있지 않다면 pop, 큐가 비어있다면 -1 출력
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)

    elif string_[0] == 'size':
        print(len(deq))
        
    elif string_[0] == 'empty':
        # 큐가 비어있으면 1, 아니면 0
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif string_[0] == 'front':
        # 큐의 가장 앞에 있는 정수 출력
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)

    elif string_[0] == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)

    else:
        print("잘못된 입력입니다.")

    