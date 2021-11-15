import sys
from collections import deque

input = sys.stdin.readline
testcase = int(input())
deq = deque()

for i in range(testcase):
    order = list(input().split())

    if order[0] == "push":
        # push(int(order[1]))
        deq.append(int(order[1]))

    elif order[0] == "pop":
        # pop() if no int in stack, print(-1)
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)

    elif order[0] == "size":
        # print()
        print(len(deq))

    elif order[0] == "empty":
        # is stack empty print(-1)
        # is stack no empty print(0)
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "top":
        # print(top) if no int in stack, print(-1)
        if len(deq) != 0:
            print(deq[len(deq) - 1])
        else:
            print(-1)